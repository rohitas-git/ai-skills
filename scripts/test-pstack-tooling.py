#!/usr/bin/env python3
"""Exercise adopted tooling against synthetic logs and disposable Git repositories."""
import csv
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / 'skills/0-implement/scripts/log-decision.py'
AUDIT = ROOT / 'skills/1-git-worktrees/scripts/worktree-audit.py'
BLIND = ROOT / 'skills/0-skill-creator/scripts/blind-packets.py'


def run(*args, cwd=None):
    return subprocess.run([str(a) for a in args], cwd=cwd, text=True, capture_output=True)


class ToolingTests(unittest.TestCase):
    def test_blind_packets_strip_metadata_and_require_matched_prompts(self):
        prepare = runpy.run_path(str(BLIND))['prepare']
        with tempfile.TemporaryDirectory() as folder:
            first, second = Path(folder) / 'model-a.json', Path(folder) / 'model-b.json'
            case = {'case_id': 'private-case-key', 'prompt': 'Summarize the checkout rules.', 'output': 'A checked explanation.', 'artifacts': {'notes.txt': 'evidence'}}
            document = {'model': 'vendor-model', 'variant': 'baseline', 'cases': [case]}
            for path in [first, second]:
                path.write_text(json.dumps(document))
            packet, mapping = prepare([('baseline', first), ('revision', second)], ['Correct behavior', 'Evidence supports claims', 'Scope preserved'])
            public = json.dumps(packet)
            for secret in ['vendor-model', 'baseline', 'revision', 'model-a.json', 'model-b.json', 'private-case-key']:
                self.assertNotIn(secret, public)
            self.assertEqual(len(mapping), 2)
            self.assertEqual(packet['options'][0]['cases'][0]['artifacts'], {'notes.txt': 'evidence'})
            document['cases'][0]['prompt'] = 'A different task'
            second.write_text(json.dumps(document))
            with self.assertRaisesRegex(ValueError, 'match exactly'):
                prepare([('baseline', first), ('revision', second)], ['A', 'B', 'C'])

    def test_blind_cli_never_overwrites_a_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            first, second, rubric = [Path(folder) / name for name in ['a.json', 'b.json', 'rubric.json']]
            for source in [first, second]:
                source.write_text(json.dumps({'cases': [{'case_id': 'one', 'prompt': 'Explain this function.', 'output': 'An explanation.'}]}))
            rubric.write_text(json.dumps(['Correctness', 'Evidence', 'Scope']))
            out = Path(folder) / 'packet'
            command = [sys.executable, BLIND, '--candidate', f'old={first}', '--candidate', f'new={second}', '--rubric', rubric, '--out', out]
            self.assertEqual(run(*command).returncode, 0)
            before = (out / 'judge.json').read_bytes()
            self.assertNotEqual(run(*command).returncode, 0)
            self.assertEqual((out / 'judge.json').read_bytes(), before)
            self.assertEqual((out / 'private-map.json').stat().st_mode & 0o777, 0o600)

    def test_statechart_deadline_stops_a_sleeping_checker_without_output(self):
        with tempfile.TemporaryDirectory() as folder:
            work = Path(folder)
            spec, config, java, jar = [work / name for name in ['Model.tla', 'Model.cfg', 'java', 'tool.jar']]
            spec.write_text('---- MODULE Model ----\nVARIABLE x\n====\n')
            config.write_text('INIT Init\nNEXT Next\n')
            jar.write_text('synthetic placeholder')
            java.write_text('#!/usr/bin/env python3\nimport time\ntime.sleep(20)\n')
            java.chmod(0o700)
            env = {**os.environ, 'JAVA': str(java), 'TLA2TOOLS': str(jar)}
            result = subprocess.run(['bun', str(ROOT / 'skills/1-statechart-modeling/scripts/statechart.ts'), str(spec), '--out', str(work / 'proof'), '--timeout', '0.2'], text=True, capture_output=True, env=env, timeout=10)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertIn('deadline', result.stderr)
            self.assertFalse((work / 'proof').exists())
            self.assertEqual(list(work.glob('.proof.statechart-*')), [])

    def test_log_keeps_one_header_and_escapes_cells(self):
        with tempfile.TemporaryDirectory() as folder:
            log = Path(folder) / 'decisions.tsv'
            for decision in ['  =HYPERLINK("bad")\nnext', '@SUM(1)']:
                result = run(sys.executable, LOG, log, 'shape', decision, 'why\twhy', 'evidence', 'kept')
                self.assertEqual(result.returncode, 0, result.stderr)
            with log.open(newline='') as handle:
                rows = list(csv.reader(handle, delimiter='\t'))
            self.assertEqual(len(rows), 3)
            self.assertTrue(all(len(row) == 6 for row in rows))
            self.assertTrue(rows[1][2].startswith("'"))
            self.assertEqual(rows[2][2], "'@SUM(1)")
            self.assertEqual(rows[1][3], 'why why')
            self.assertEqual(log.stat().st_mode & 0o777, 0o600)

    def test_log_refuses_links_and_unrelated_files(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'protected.txt'
            target.write_text('keep me\n')
            link = Path(folder) / 'link.tsv'
            link.symlink_to(target)
            for path in [target, link]:
                result = run(sys.executable, LOG, path, 'a', 'b', 'c', 'd', 'e')
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(target.read_text(), 'keep me\n')

    def test_concurrent_log_appends_do_not_duplicate_header(self):
        with tempfile.TemporaryDirectory() as folder:
            log = Path(folder) / 'decisions.tsv'
            processes = [subprocess.Popen([sys.executable, str(LOG), str(log), 'phase', str(i), 'why', 'proof', 'kept'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) for i in range(8)]
            outcomes = [(process, process.communicate(timeout=15)) for process in processes]
            for process, (_, stderr) in outcomes:
                self.assertEqual(process.returncode, 0, stderr)
            self.assertEqual(len(log.read_text().splitlines()), 9)
            self.assertEqual(log.read_text().count('ts\tphase\tdecision'), 1)

    def test_audit_preserves_refs_and_treats_untracked_as_work(self):
        with tempfile.TemporaryDirectory(prefix='worktree audit ') as folder:
            repo, worktree = Path(folder) / 'repo', Path(folder) / 'branch with spaces'
            self.assertEqual(run('git', 'init', '-b', 'main', repo).returncode, 0)
            for key, value in [('user.name', 'Fixture'), ('user.email', 'fixture@example.invalid')]:
                self.assertEqual(run('git', 'config', key, value, cwd=repo).returncode, 0)
            (repo / 'file.txt').write_text('initial\n')
            self.assertEqual(run('git', 'add', 'file.txt', cwd=repo).returncode, 0)
            self.assertEqual(run('git', 'commit', '-m', 'fixture', cwd=repo).returncode, 0)
            self.assertEqual(run('git', 'worktree', 'add', '-b', 'topic', worktree, cwd=repo).returncode, 0)
            (worktree / 'untracked.txt').write_text('valuable work\n')
            before = run('git', 'show-ref', cwd=repo).stdout
            result = run(sys.executable, AUDIT, '--base', 'main', repo)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            row = next(row for row in report['worktrees'] if row['path'] == str(worktree.resolve()))
            self.assertTrue(row['ancestor_of_base'])
            self.assertEqual(row['disposition'], 'hold-dirty')
            self.assertEqual(row['untracked'], 1)
            self.assertEqual(before, run('git', 'show-ref', cwd=repo).stdout)
            self.assertEqual((worktree / 'untracked.txt').read_text(), 'valuable work\n')
            self.assertFalse(report['network_used'])
            invalid = run(sys.executable, AUDIT, '--base', 'missing', repo)
            self.assertNotEqual(invalid.returncode, 0)


if __name__ == '__main__':
    unittest.main()
