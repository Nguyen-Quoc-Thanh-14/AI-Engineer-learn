#!/usr/bin/env python3
"""Check deterministic output semantics for selected beginner demo lessons."""
from pathlib import Path
import json, subprocess, sys, tempfile, os
ROOT=Path(__file__).resolve().parents[1]
ORACLES=json.loads(Path(__file__).with_name('output_oracles.json').read_text(encoding='utf8'))
def run():
    results=[]
    for k,expected in ORACLES.items():
        cases=list(ROOT.glob('03_HOC_PHAN/**/MA_MAU/'+k+'_demo.py'))
        if len(cases)!=1:
            results.append({'id':k,'status':'MISSING_OR_DUPLICATE','found':len(cases)})
            continue
        with tempfile.TemporaryDirectory(prefix='oracle_') as td:
            try:
                p=subprocess.run([sys.executable,'-I',str(cases[0])], cwd=td,
                                 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},
                                 capture_output=True,text=True,timeout=7)
                success=p.returncode==0 and p.stdout==expected
                results.append({'id':k,'status':'PASS_ORACLE' if success else 'FAIL_ORACLE',
                                'actual':p.stdout[-500:],'expected':expected,
                                'exit_code':p.returncode,'stderr':p.stderr[-300:]})
            except subprocess.TimeoutExpired:
                results.append({'id':k,'status':'TIMEOUT'})
    fn=Path(__file__).with_name('ORACLE_RESULTS.json')
    fn.write_text(json.dumps({'python':sys.version,'results':results},ensure_ascii=False,indent=2),encoding='utf8')
    print('Saved',fn,'pass',sum(r['status']=='PASS_ORACLE' for r in results),'/',len(results))
    return int(any(r['status']!='PASS_ORACLE' for r in results))
if __name__=='__main__':raise SystemExit(run())
