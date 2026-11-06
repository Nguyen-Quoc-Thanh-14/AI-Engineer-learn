"""H06.01 B: Hypothesis length invariant and real shrinking of broken sorter."""
from __future__ import annotations
from hypothesis import find, given, settings, strategies as st

def broken_sort(values: list[int]) -> list[int]:
    """Deliberately WRONG: drops one element from any nonempty list."""
    return sorted(values)[:-1]

@given(st.lists(st.integers(min_value=-100, max_value=100), max_size=30))
@settings(max_examples=100, derandomize=True, deadline=None)
def test_builtin_sorted_keeps_length(xs):
    assert len(sorted(xs)) == len(xs)

def shrink_counterexample() -> list[int]:
    example = find(
        st.lists(st.integers(min_value=-100,max_value=100), min_size=1, max_size=15),
        lambda xs: len(broken_sort(xs)) != len(xs),
        settings=settings(max_examples=200,derandomize=True,deadline=None,database=None),
    )
    assert len(example)==1, example
    assert len(broken_sort(example))==0
    return example

if __name__=="__main__":
    test_builtin_sorted_keeps_length()
    print("H06.01_HYPOTHESIS_SHRINK_PASS",shrink_counterexample())
