import argparse
from pathlib import Path

def build_parser():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path)
    p.add_argument('--dry-run',action='store_true');return p
p=build_parser();args=p.parse_args(['--input','report.csv','--dry-run'])
assert args.input==Path('report.csv') and args.dry_run
try:p.parse_args(['--unknown'])
except SystemExit as e:assert e.code==2
else:raise AssertionError('unknown option accepted')
