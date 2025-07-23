import os
import sys
import yaml
from pathlib import Path
import re

def extract_alerts_from_file(file_path):
    alerts_by_group = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = yaml.safe_load(f)

    groups = content.get('groups', [])
    for group in groups:
        group_name = group.get('name', 'UnnamedGroup')
        rules = group.get('rules', [])
        for rule in rules:
            if 'alert' in rule:
                alert_name = rule['alert']
                summary = rule.get('annotations', {}).get('summary', '')
                description = rule.get('annotations', {}).get('description', '')
                severity = rule.get('labels', {}).get('severity', '')
                alerts_by_group.setdefault(group_name, []).append({
                    'alert': alert_name,
                    'summary': summary,
                    'description': description,
                    'severity': severity
                })
    return alerts_by_group

def extract_from_directory(directory):
    all_alerts = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.yaml', '.yml')):
                path = os.path.join(root, filename)
                group_alerts = extract_alerts_from_file(path)
                for group_name, alerts in group_alerts.items():
                    all_alerts.setdefault(group_name, []).extend(alerts)
    return all_alerts

def github_anchor(text):
    """Generate GitHub-compatible anchor link"""
    anchor = text.strip().lower()
    anchor = re.sub(r'[^\w\- ]', '', anchor)
    anchor = anchor.replace(' ', '-')
    return anchor

def generate_markdown(alerts_by_group, output_file):
    def escape_liquid(text):
        """
        Escape {{ and }} unless they are inside inline code blocks (`...`).
        """
        def replacer(match):
            segment = match.group(0)
            if segment.startswith('`') and segment.endswith('`'):
                return segment  # Don't escape inside backticks
            # Escape {{ and }} outside backticks
            return segment.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')

        # Match either `inline code` or everything else
        return ''.join(replacer(m) for m in re.finditer(r'`[^`]*`|[^`]+', text))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'<a name="top"></a>\n')
        f.write(f'<p style="font-size: 28px; font-weight: bold;">Prometheus Alert Documentation</p>\n\n')

        # Alert Tables
        for group_name in sorted(alerts_by_group.keys()):
            f.write(f'## {group_name}\n')
            f.write('| Alert Name | Summary | Description | Severity |\n')
            f.write('| :--- | :--- | :--- | :--- |')
            for alert in sorted(alerts_by_group[group_name], key=lambda a: a['alert']):
                alert_name = alert["alert"].replace('|', '\\|')
                summary = escape_liquid(alert["summary"].replace('|', '\\|').replace('\n', '<br>')) if alert["summary"] else ''
                description = escape_liquid(alert["description"].replace('|', '\\|').replace('\n', '<br>')) if alert["description"] else ''
                severity = alert["severity"].replace('|', '\\|')
                f.write(f'\n| **{alert_name}** | {summary} | {description} | {severity} |')
            f.write('\n<p align="right"><a href="#top">🔝 Back to Top</a></p>\n')
            f.write('\n---\n\n')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate Markdown tables for Prometheus alert groups with TOC.')
    parser.add_argument('input_path', help='YAML file or directory containing alert rules')
    parser.add_argument('-o', '--output', default='alerts.md', help='Output Markdown file')
    args = parser.parse_args()

    input_path = Path(args.input_path)

    if input_path.is_dir():
        alerts = extract_from_directory(str(input_path))
    elif input_path.is_file():
        alerts = extract_alerts_from_file(str(input_path))
    else:
        print(f"Error: {args.input_path} is not a valid file or directory.")
        sys.exit(1)

    generate_markdown(alerts, args.output)
    print(f"Markdown file generated: {args.output}")
