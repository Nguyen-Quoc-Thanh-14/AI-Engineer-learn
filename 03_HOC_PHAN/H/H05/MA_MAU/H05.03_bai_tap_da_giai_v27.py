# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def normalize(text): return ' '.join(text.split())
def count_words(text): return len(normalize(text).split())
def count_words_original(text): return len(text.split())
for s in ('','x',' a  b ','\t a\n b\t'):
    assert count_words(s)==count_words_original(s)
print('PASS H05.03')
