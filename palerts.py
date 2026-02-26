import os
import sys
import yaml
from pathlib import Path


def extract_alerts_from_file(file_path):
    alerts_by_group = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = yaml.safe_load(f)

    groups = content.get('groups', [])
    # for group in groups:
    #     group_name = group.get('name', 'UnnamedGroup')
    #     rules = group.get('rules', [])
    #     for rule in rules:
    #         if 'alert' in rule:
    #             alert_name = rule['alert']
    #             summary = rule.get('annotations', {}).get('summary', '')
    #             description = rule.get('annotations', {}).get('description', '')
    #             severity = rule.get('labels', {}).get('severity', '')
    #             alerts_by_group.setdefault(group_name, []).append({
    #                 'alert': alert_name,
    #                 'summary': summary,
    #                 'description': description,
    #                 'severity': severity
    #             })
    return groups


def extract_from_directory(directory):
    all_alerts = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.yaml', '.yml')):
                path = os.path.join(root, filename)
                group_alerts = extract_alerts_from_file(path)
                all_alerts.append(group_alerts)
    return all_alerts


def build_alert_dir(groups, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for group in groups:
        if len(group) >= 1:
            group_name = group[0].get(
                'name', 'UnnamedGroup').replace(' ', '_').lower()

            rules = group[0].get('rules', [])
        else:
            group_name = group.get(
                'name', 'UnnamedGroup').replace(' ', '_').lower()
            rules = group.get('rules', [])

        for rule in rules:
            grp_out = {}
            if 'alert' in rule:
                ruleadj = {}
                group_dir = output_dir + '/alerts/' + group_name
                os.makedirs(group_dir, exist_ok=True)
                alert_name = rule['alert'].replace(' ', '_').lower()
                alert_file = alert_name + '.yaml'
                ruleadj['alert'] = alert_name

                rule['annotations'].update({
                    # 'summary': rule[
                    #     'annotations']['summary'].replace('\n', ''),
                    # 'description': rule[
                    #     'annotations']['description'].replace('\n', ''),
                    'runbook_url': 'default_runbook_url',
                    'dashboard_url': 'default_dashboard_url'
                })
                rule['labels'].update({
                    'rackspace_com_coreAccountID': 'default_coreID',
                    'rackspace_com_overseerID': 'default_overseerID',
                    'group_name': 'default_group_name',
                    'node_name': 'default_node_name',
                    'pod_name': 'default_pod_name',
                    'severity': 'warning'
                })
                ruleadj['labels'] = rule['labels']
                ruleadj['expr'] = rule['expr']
                rule.setdefault('for', '0m')
                ruleadj['for'] = rule['for']
                ruleadj['annotations'] = rule['annotations']
            else:
                group_dir = output_dir + '/recording/' + group_name
                os.makedirs(group_dir, exist_ok=True)
                alert_file = rule['record'].replace(':', '').lower() + '.yaml'
                ruleadj = rule

            grp_out['groups'] = [{'name': group_name, 'rules': [ruleadj]}]
            with open(group_dir + '/' + alert_file, "w") as f:
                yaml.dump(grp_out, f, default_flow_style=False,
                                    sort_keys=False)
    print('DONE PROCESSING RULES...')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='split prometheus alert file into individual files')
    parser.add_argument('input_path',
                        help='YAML file or directory containing alert rules')
    parser.add_argument('-o', '--output',
                        default='/tmp/alertsout',
                        help='Output alerts directory')
    args = parser.parse_args()

    input_path = Path(args.input_path)

    if input_path.is_dir():
        alerts = extract_from_directory(str(input_path))
    elif input_path.is_file():
        alerts = extract_alerts_from_file(str(input_path))
    else:
        print(f"Error: {args.input_path} is not a valid file or directory.")
        sys.exit(1)

    build_alert_dir(alerts, args.output)
    print(f"Files generated in: {args.output}")
