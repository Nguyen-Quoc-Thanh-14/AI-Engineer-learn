# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
labels={
 'q1':('supported','answer has citation'),
 'q2':('unsupported','model invented fact'),
 'q3':('conflicting','two sources disagree'),
 'q4':('insufficient_evidence','no grounded answer')}
assert len(labels)==4
assert set(t for t,_ in labels.values())=={'supported','unsupported','conflicting','insufficient_evidence'}
assert all(note for _,note in labels.values())
print('PASS PN04.02')
