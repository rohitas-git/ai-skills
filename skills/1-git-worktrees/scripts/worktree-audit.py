#!/usr/bin/env python3
"""Inspect local worktrees without fetching, reading chats, or deleting. Adapted from pstack (MIT)."""
import argparse
import json
import os
from pathlib import Path
import subprocess


def git(repo, *args):
    result = subprocess.run(['git', '--no-optional-locks', '-C', str(repo), *args], capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise ValueError(result.stderr.strip() or f'git exited {result.returncode}')
    return result.stdout


def inspect_worktrees(repo, base):
    base_sha = git(repo, 'rev-parse', '--verify', '--end-of-options', f'{base}^{{commit}}').strip()
    records = []
    current = {}
    for field in git(repo, 'worktree', 'list', '--porcelain', '-z').split('\0'):
        if not field:
            if current:
                records.append(current)
                current = {}
            continue
        key, _, value = field.partition(' ')
        current[key] = value
    if current:
        records.append(current)
    rows = []
    for index, record in enumerate(records):
        folder = record['worktree']
        row = {'path': folder, 'head': record.get('HEAD'), 'branch': record.get('branch'),
               'primary': index == 0, 'locked': 'locked' in record, 'prunable': 'prunable' in record,
               'ancestor_of_base': None, 'tracked_changes': None, 'untracked': None}
        try:
            status = git(folder, 'status', '--porcelain=v1', '-z', '--untracked-files=all').split('\0')
            tracked = untracked = 0
            iterator = iter(status)
            for item in iterator:
                if not item:
                    continue
                if item.startswith('??'):
                    untracked += 1
                else:
                    tracked += 1
                    if 'R' in item[:2] or 'C' in item[:2]:
                        next(iterator, None)
            ancestor = subprocess.run(['git', '--no-optional-locks', '-C', folder, 'merge-base', '--is-ancestor', row['head'], base_sha], capture_output=True, timeout=30)
            if ancestor.returncode not in (0, 1):
                raise ValueError('cannot determine base ancestry')
            row.update(ancestor_of_base=ancestor.returncode == 0, tracked_changes=tracked, untracked=untracked)
            row['disposition'] = ('hold-primary' if row['primary'] else
                                  'hold-locked' if row['locked'] else
                                  'hold-dirty' if tracked or untracked else
                                  'hold-prunable' if row['prunable'] else 'review')
        except (OSError, ValueError, subprocess.TimeoutExpired) as error:
            row.update(disposition='unknown', error=str(error))
        rows.append(row)
    return {'base': base, 'base_sha': base_sha, 'network_used': False,
            'scope': 'Local refs only; ancestry does not prove a PR was merged or authorize cleanup.',
            'worktrees': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, help='existing local ref; never fetched')
    parser.add_argument('repo', nargs='?', type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        report = inspect_worktrees(args.repo, args.base)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        parser.exit(2, f'{error}\n')
    print(json.dumps(report, indent=2))
    return 1 if any(row['disposition'] == 'unknown' for row in report['worktrees']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
