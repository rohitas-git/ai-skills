#!/usr/bin/env python3
"""Prepare matched, metadata-blinded review packets. Inspired by pstack's eval playbook (MIT)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets


def prepare(candidates, rubric):
    if len(candidates) < 2 or len({name for name, _ in candidates}) != len(candidates):
        raise ValueError('provide at least two uniquely named candidates')
    if not isinstance(rubric, list) or not 3 <= len(rubric) <= 6 or not all(isinstance(item, str) and item.strip() for item in rubric):
        raise ValueError('rubric must contain three to six concrete criteria')
    records = []
    expected = None
    for name, source in candidates:
        source_bytes = source.read_bytes()
        if len(source_bytes) > 4 * 1024 * 1024:
            raise ValueError('candidate exports must be at most 4 MiB')
        data = json.loads(source_bytes)
        cases = data.get('cases')
        if not isinstance(cases, list) or not cases:
            raise ValueError('candidate must contain a nonempty cases list')
        normalized = {}
        for case in cases:
            key = case.get('case_id')
            if not isinstance(key, str) or not key or key in normalized:
                raise ValueError('case identities must be unique nonempty strings')
            if not isinstance(case.get('prompt'), str) or not isinstance(case.get('output'), str):
                raise ValueError('each case needs a prompt and output')
            artifacts = case.get('artifacts', {})
            if not isinstance(artifacts, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in artifacts.items()):
                raise ValueError('artifacts must map names to reviewed text')
            normalized[key] = {'prompt': case['prompt'], 'output': case['output'], 'artifacts': artifacts}
        prompts = {key: value['prompt'] for key, value in normalized.items()}
        if expected is not None and prompts != expected:
            raise ValueError('candidate cases and prompts must match exactly')
        expected = prompts
        records.append((name, source, normalized, hashlib.sha256(source_bytes).hexdigest()))
    secrets.SystemRandom().shuffle(records)
    mapping, packets = {}, []
    for index, (name, source, cases, source_hash) in enumerate(records, 1):
        label = f'Option {index}'
        mapping[label] = {'candidate': name, 'source': str(source.resolve()), 'sha256': source_hash}
        packets.append({'label': label, 'cases': [{'task': f'Task {i}', **case} for i, (_, case) in enumerate(sorted(cases.items()), 1)]})
    return {'schema_version': 1, 'rubric': rubric, 'options': packets,
            'scope': 'Metadata-blinded only. Screen prompts, outputs and artifact text for identity leakage before judging. Score all options together; do not infer execution from self-report.'}, mapping


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', action='append', required=True, metavar='NAME=FILE')
    parser.add_argument('--rubric', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True, help='new private directory; never overwritten')
    args = parser.parse_args()
    try:
        candidates = []
        for value in args.candidate:
            name, separator, file = value.partition('=')
            if not separator or not name or not file:
                raise ValueError('candidate must be NAME=FILE')
            candidates.append((name, Path(file)))
        packet, mapping = prepare(candidates, json.loads(args.rubric.read_text()))
        args.out.mkdir(mode=0o700)
        for name, data in [('judge.json', packet), ('private-map.json', mapping)]:
            with (args.out / name).open('x', encoding='utf-8') as handle:
                os.chmod(handle.name, 0o600)
                json.dump(data, handle, indent=2)
                handle.write('\n')
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(2, f'{error}\n')
    print(f'Created {args.out / "judge.json"}; give only that file to the judge. Keep private-map.json private.')


if __name__ == '__main__':
    main()
