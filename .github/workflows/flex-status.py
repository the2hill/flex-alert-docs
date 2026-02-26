#!/usr/bin/env python3
"""
Fetch Rackspace OpenStack Flex status from the ServiceNow SP page API.
Writes result to docs/flex-status.json.

Usage:
    python3 fetch_rackspace_status.py
    python3 fetch_rackspace_status.py --output /path/to/flex-status.json
    python3 fetch_rackspace_status.py --dump-outages
    python3 fetch_rackspace_status.py --dump-status
    python3 fetch_rackspace_status.py --dump-raw
    python3 fetch_rackspace_status.py --mock-active   # simulate active event for local testing
"""

import urllib.request
import urllib.error
import json
import re
import time
import argparse
from datetime import datetime, timezone

# ── Constants ─────────────────────────────────────────────────────────────────
SERVICE_SYS_ID  = "85be01de87aaee104b7afc45dabb35b8"
PORTAL_ID       = "4e1bfc68db0172006bb3fb0bbf9619ae"
SNOW_BASE       = "https://rackspace.service-now.com"
STATUS_PAGE_URL = f"{SNOW_BASE}/system_status?id=service_status&service={SERVICE_SYS_ID}"

HEADERS = {
    "User-Agent":      "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept":          "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":   "no-cache",
    "Referer":         STATUS_PAGE_URL,
}

COLOR_MAP = {
    "green":   "operational",
    "yellow":  "degraded",
    "orange":  "degraded",
    "red":     "outage",
    "blue":    "maintenance",
    "grey":    "unknown",
    "gray":    "unknown",
    "#5cb85c": "operational",
    "#f0ad4e": "degraded",
    "#d9534f": "outage",
    "#337ab7": "maintenance",
    "#5bc0de": "maintenance",
    "#777":    "unknown",
    "#777777": "unknown",
}

MOCK_EVENT = {
    "title":         "OpenStack Flex | DFW3, SJC3 | February 26, 2026",
    "details":       "Rackspace will be performing a Service Disrupting maintenance in our DFW3, SJC3 data centers. During this maintenance, OpenStack Flex customers may experience disruptions to compute, network, and storage services.",
    "begin_display": "2026-02-25 20:00:00",
    "end_display":   "2026-02-26 08:00:00",
    "begin_value":   "2026-02-26 02:00:00",
    "end_value":     "2026-02-26 14:00:00",
    "duration":      "12 hours",
    "date":          "February 26, 2026",
    "link":          STATUS_PAGE_URL,
    "mock":          True,
}


# ── HTTP ──────────────────────────────────────────────────────────────────────
def fetch_page():
    ts  = int(time.time() * 1000)
    url = (
        f"{SNOW_BASE}/api/now/sp/page"
        f"?id=service_status"
        f"&service={SERVICE_SYS_ID}"
        f"&time={ts}"
        f"&portal_id={PORTAL_ID}"
        f"&request_uri=%2Fsystem_status%3Fid%3Dservice_status%26service%3D{SERVICE_SYS_ID}"
    )
    print(f"[fetch] GET {url}")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw  = r.read()
        text = raw.decode(r.headers.get_content_charset("utf-8"), errors="replace")
        print(f"[fetch] HTTP {r.status} — {len(raw):,} bytes")
        return json.loads(text)


# ── Navigation helpers ─────────────────────────────────────────────────────────
def dig(obj, *path, default=None):
    cur = obj
    for step in path:
        try:
            cur = cur[step]
        except (KeyError, IndexError, TypeError):
            return default
    return cur


def get_status_widget_data(result):
    return dig(result, "containers", 1, "rows", 0, "columns", 0, "widgets", 0, "widget", "data")


def get_history_widget_data(result):
    return dig(result, "containers", 1, "rows", 1, "columns", 0, "widgets", 1, "widget", "data")


# ── Date parsing ──────────────────────────────────────────────────────────────
def parse_dt(value):
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        ts = float(value)
        if ts > 1e10:
            ts /= 1000.0
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    s = str(value).strip()
    if not s:
        return None
    if re.match(r'^\d+$', s):
        ts = float(s)
        if ts > 1e10:
            ts /= 1000.0
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    for fmt in (None, "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%B %d, %Y %H:%M", "%B %d, %Y"):
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00")) if fmt is None else datetime.strptime(s, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except (ValueError, AttributeError):
            continue
    return None


def is_now_in_window(begin_value, end_value, now):
    dt_start = parse_dt(begin_value)
    dt_end   = parse_dt(end_value)
    if dt_start and dt_start > now:
        return False
    if dt_end and dt_end < now:
        return False
    return True


# ── Color resolution ──────────────────────────────────────────────────────────
def resolve_color(raw_color):
    if not raw_color:
        return "unknown", raw_color
    key = str(raw_color).strip().lower()
    if key in COLOR_MAP:
        return COLOR_MAP[key], raw_color
    if key.startswith("#") and len(key) in (4, 7):
        try:
            hex_val = key.lstrip("#")
            if len(hex_val) == 3:
                hex_val = "".join(c * 2 for c in hex_val)
            r, g, b = int(hex_val[0:2], 16), int(hex_val[2:4], 16), int(hex_val[4:6], 16)
            if g > r and g > b:
                return "operational", raw_color
            elif r > g and r > b:
                return "outage", raw_color
            elif r > 150 and g > 100 and b < 80:
                return "degraded", raw_color
            elif b > r and b > g:
                return "maintenance", raw_color
        except (ValueError, IndexError):
            pass
    return key, raw_color


# ── Processing ────────────────────────────────────────────────────────────────
def process_current_status(data):
    if not data:
        return None
    days = data.get("days", [])
    if not days:
        return None
    today = days[-1]   # days[] is oldest-first; last entry is today
    status, color_raw = resolve_color(today.get("color", ""))
    return {
        "status":    status,
        "color_raw": color_raw,
        "message":   today.get("msg", ""),
        "date":      today.get("date", ""),
    }


def process_outages(data, now):
    if not data:
        return None
    for outage in data.get("outages", []):
        if not isinstance(outage, dict):
            continue
        info = outage.get("info", {})
        if not isinstance(info, dict):
            continue
        if is_now_in_window(info.get("beginValue"), info.get("endValue"), now):
            return {
                "title":         info.get("title", "OpenStack Flex Event"),
                "details":       info.get("details", ""),
                "begin_display": info.get("beginDisplay", ""),
                "end_display":   info.get("endDisplay", ""),
                "begin_value":   info.get("beginValue"),
                "end_value":     info.get("endValue"),
                "duration":      info.get("duration", ""),
                "date":          info.get("date", outage.get("outageDate", "")),
                "link":          STATUS_PAGE_URL,
            }
    return None


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Fetch Rackspace OpenStack Flex status")
    parser.add_argument("--output",       default="docs/flex-status.json")
    parser.add_argument("--dump-outages", action="store_true")
    parser.add_argument("--dump-status",  action="store_true")
    parser.add_argument("--dump-raw",     action="store_true")
    parser.add_argument("--mock-active",  action="store_true",
                        help="Write a mock active event — use this to test the banner locally")
    args = parser.parse_args()

    # ── Mock mode — skip fetch entirely ──────────────────────────────────────
    if args.mock_active:
        now    = datetime.now(timezone.utc)
        output = {
            "fetched_at":     now.isoformat(),
            "current_status": {"status": "maintenance", "color_raw": "#337ab7", "message": "Maintenance in progress", "date": now.strftime("%Y-%m-%d")},
            "active_event":   MOCK_EVENT,
        }
        print("\n-- Mock result --")
        print(json.dumps(output, indent=2, default=str))
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"\nWrote mock -> {args.output}")
        print(f"Run 'mkdocs serve' and check the banner on api-status.md")
        print(f"When done, run without --mock-active to restore live data.")
        return

    # ── Live fetch ────────────────────────────────────────────────────────────
    try:
        page_data = fetch_page()
    except Exception as e:
        print(f"[error] Failed to fetch page: {e}")
        output = {
            "fetched_at":     datetime.now(timezone.utc).isoformat(),
            "error":          str(e),
            "current_status": None,
            "active_event":   None,
        }
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"Wrote empty result -> {args.output}")
        return

    result_root  = page_data.get("result", {})
    status_data  = get_status_widget_data(result_root)
    history_data = get_history_widget_data(result_root)

    # ── Debug modes ───────────────────────────────────────────────────────────
    if args.dump_raw:
        print("\n=== Status widget data ===")
        print(json.dumps(status_data, indent=2, default=str))
        print("\n=== History widget data (first 3 outages) ===")
        if history_data:
            preview = dict(history_data)
            preview["outages"] = preview.get("outages", [])[:3]
            print(json.dumps(preview, indent=2, default=str))
        return

    if args.dump_status:
        days = (status_data or {}).get("days", [])
        print(f"{len(days)} day(s) in status widget:\n")
        for i, d in enumerate(days):
            status, _ = resolve_color(d.get("color", ""))
            marker = "  <-- today" if i == len(days) - 1 else ""
            print(f"  [{i}] date={d.get('date')}  color={d.get('color')!r}  ->  {status}  msg={d.get('msg','')!r}{marker}")
        return

    if args.dump_outages:
        outages = (history_data or {}).get("outages", [])
        now     = datetime.now(timezone.utc)
        print(f"{len(outages)} outage(s) found:\n")
        for i, o in enumerate(outages):
            info   = o.get("info", {}) if isinstance(o, dict) else {}
            begin  = info.get("beginValue")
            end    = info.get("endValue")
            active = is_now_in_window(begin, end, now)
            marker = "  <-- ACTIVE NOW" if active else ""
            print(f"[{i}] {info.get('title', '?')}{marker}")
            print(f"     beginValue={begin!r}  ->  {parse_dt(begin)}")
            print(f"     endValue={end!r}    ->  {parse_dt(end)}")
            print(f"     beginDisplay={info.get('beginDisplay')!r}")
            print(f"     endDisplay={info.get('endDisplay')!r}")
            print(f"     details={str(info.get('details', ''))[:120]!r}")
            print()
        return

    # ── Normal run ────────────────────────────────────────────────────────────
    now            = datetime(2026, 2, 26, 8, 0, tzinfo=timezone.utc)
    current_status = process_current_status(status_data)
    active_event   = process_outages(history_data, now)

    output = {
        "fetched_at":     now.isoformat(),
        "current_status": current_status,
        "active_event":   active_event,
    }

    print("\n-- Final result --")
    print(json.dumps(output, indent=2, default=str))

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nWrote -> {args.output}")


if __name__ == "__main__":
    main()
