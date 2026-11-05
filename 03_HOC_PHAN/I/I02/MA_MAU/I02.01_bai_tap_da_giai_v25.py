"""I02.01 corrected: find first position >= x, including absent targets."""
from bisect import bisect_left

def lower_bound(values: list[int], target: int) -> int:
    """Precondition: values is sorted in nondecreasing order."""
    return bisect_left(values, target)

def check():
    assert lower_bound([1, 2, 2, 3], 2) == 1
    assert lower_bound([1, 3, 5], 4) == 2  # absent target, valid insertion position
    assert lower_bound([], 5) == 0
    assert lower_bound([2, 2, 2], 2) == 0
    assert lower_bound([2, 2, 2], 3) == 3
    for values in ([], [3], [1,1,1], [-3,-1,0,7], list(range(50))):
        for x in range(-6, 55):
            want = next((i for i,v in enumerate(values) if v>=x),len(values))
            assert lower_bound(values,x)==want,(values,x,want)
if __name__=="__main__":
    check()
    print("PASS I02.01 lower_bound")
