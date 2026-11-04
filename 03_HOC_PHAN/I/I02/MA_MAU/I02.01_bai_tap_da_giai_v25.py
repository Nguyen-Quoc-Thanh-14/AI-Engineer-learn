# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def first_index(sorted_values: list[int], target: int) -> int:
    lo, hi = 0, len(sorted_values)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_values[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(sorted_values) and sorted_values[lo] == target:
        return lo
    return -1

def check():
    assert first_index([1, 2, 2, 3], 2) == 1
    assert first_index([], 1) == -1
    assert first_index([1, 3, 5], 4) == -1
    assert first_index([-2, 0, 0], -2) == 0
    for nums in ([], [1], [1,1,1], [-3,-1,0,7], list(range(30))):
        for v in range(-4, 32):
            want = nums.index(v) if v in nums else -1
            assert first_index(nums, v) == want

if __name__ == '__main__':
    check()
    print('OK I02.01')
