---
hide:
  - navigation
  - toc
---
<div id="rax-flex-banner"></div>

<script>
(function () {
  var JSON_URL = 'flex-alert-docs/flex-status.json';

  var IMPACT_STYLE = {
    critical:             { bg: '#7f0000', border: '#ff1744', label: '🔴 Critical Incident'     },
    major:                { bg: '#7f0000', border: '#ff1744', label: '🔴 Major Incident'         },
    minor:                { bg: '#e65100', border: '#ff9100', label: '🟠 Minor Incident'         },
    maintenance:          { bg: '#1a237e', border: '#448aff', label: '🔧 Scheduled Maintenance'  },
    in_progress:          { bg: '#1a237e', border: '#448aff', label: '🔧 Maintenance In Progress'},
    none:                 { bg: '#2e7d32', border: '#69f0ae', label: '✅ Operational'            },
  };
  var DEFAULT_STYLE = { bg: '#b71c1c', border: '#ff5252', label: '⚠️ Active Incident' };

  function style(impact, isMaint) {
    if (isMaint) return IMPACT_STYLE['maintenance'];
    return IMPACT_STYLE[(impact||'').toLowerCase()] || DEFAULT_STYLE;
  }

  function fmtDate(iso) {
    if (!iso) return '';
    try { return new Date(iso).toUTCString(); } catch(e) { return iso; }
  }

  function esc(s) {
    return String(s||'')
      .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  function buildBanner(event, isMaint) {
    var s       = style(event.impact, isMaint);
    var title   = esc(event.name || (isMaint ? 'Scheduled Maintenance' : 'Active Incident'));
    var status  = esc(event.status || '');
    var impact  = esc(event.impact || '');
    var created = fmtDate(event.created_at || event.scheduled_for);
    var until   = isMaint ? fmtDate(event.scheduled_until) : '';
    var latest  = esc(event.latest_update || '');
    var link    = event.shortlink
                  ? event.shortlink
                  : 'https://rackspace.service-now.com/system_status?id=service_status&service=85be01de87aaee104b7afc45dabb35b8';
    var updates = event.updates || [];

    // Build update history accordion
    var historyHtml = '';
    if (updates.length > 1) {
      historyHtml = '<details style="margin-top:10px;">' +
        '<summary style="cursor:pointer;font-size:0.85em;opacity:0.85;">Show all updates (' + updates.length + ')</summary>' +
        '<div style="margin-top:8px;border-top:1px solid rgba(255,255,255,0.2);padding-top:8px;">';
      updates.forEach(function(u) {
        historyHtml +=
          '<div style="margin-bottom:10px;">' +
          '<span style="font-size:0.8em;opacity:0.75;">' + fmtDate(u.created_at) + ' — ' + esc(u.status||'') + '</span>' +
          '<div style="font-size:0.88em;margin-top:2px;">' + esc(u.body||'') + '</div>' +
          '</div>';
      });
      historyHtml += '</div></details>';
    }

    return '<div style="' +
        'background:' + s.bg + ';' +
        'color:#fff;' +
        'border-left:5px solid ' + s.border + ';' +
        'padding:14px 18px;' +
        'border-radius:0 6px 6px 0;' +
        'margin-bottom:20px;' +
        'font-family:inherit;' +
      '">' +
      // Header row
      '<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:6px;">' +
        '<strong style="font-size:1.05em;">' + s.label + ' — OpenStack Flex</strong>' +
        '<span style="font-size:0.82em;opacity:0.8;">' +
          (status ? 'Status: <strong>' + status + '</strong>' : '') +
          (impact && impact !== status ? (status ? ' &nbsp;·&nbsp; ' : '') + 'Impact: <strong>' + impact + '</strong>' : '') +
        '</span>' +
      '</div>' +
      // Title
      '<div style="margin-top:8px;font-size:1em;font-weight:600;">' + title + '</div>' +
      // Timestamps
      '<div style="margin-top:4px;font-size:0.82em;opacity:0.8;">' +
        (created ? (isMaint ? 'Starts: ' : 'Opened: ') + created : '') +
        (until   ? ' &nbsp;·&nbsp; Until: ' + until : '') +
      '</div>' +
      // Latest update
      (latest ? '<div style="margin-top:10px;font-size:0.9em;background:rgba(0,0,0,0.2);padding:8px 12px;border-radius:4px;">' +
        '<strong>Latest update:</strong><br>' + latest +
      '</div>' : '') +
      // History accordion
      historyHtml +
      // Footer link
      '<div style="margin-top:12px;font-size:0.82em;">' +
        '<a href="' + link + '" target="_blank" rel="noopener" style="color:#fff;opacity:0.85;text-decoration:underline;">' +
          'View full details on Rackspace Status →' +
        '</a>' +
      '</div>' +
    '</div>';
  }

  fetch(JSON_URL + '?_=' + Date.now())
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      var banner = document.getElementById('rax-flex-banner');
      if (!banner) return;
      if (data.active_incident) {
        banner.innerHTML = buildBanner(data.active_incident, false);
      } else if (data.active_maintenance) {
        banner.innerHTML = buildBanner(data.active_maintenance, true);
      }
      // If both null, banner stays empty — no noise during normal operations
    })
    .catch(function (e) {
      console.warn('[rax-status] Could not load status:', e);
    });
})();
</script>
# Welcome to the Flex Alerts Documentation
