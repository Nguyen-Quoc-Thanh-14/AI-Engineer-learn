# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def normalize(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError('phải là str')
    return ' '.join(s.casefold().split())

def exact_match_score(pairs: list[tuple[str,str]]) -> float:
    if not pairs:
        raise ValueError('không có mẫu đánh giá')
    return sum(normalize(a) == normalize(b) for a,b in pairs) / len(pairs)

def check():
    assert exact_match_score([('Paris', ' PARIS ')]) == 1.0
    assert exact_match_score([('Hà Nội', 'Hồ Chí Minh')]) == 0.0
    assert exact_match_score([('two', '2'), ('yes', 'yes')]) == 0.5
    try: exact_match_score([])
    except ValueError: pass
    else: raise AssertionError('dataset rỗng')

if __name__ == '__main__':
    check()
    print('OK PN03.01')
