from itertools import combinations
for n in range(9):
    universe=tuple(range(n))
    subsets=[combo for r in range(n+1) for combo in combinations(universe,r)]
    assert len(subsets)==2**n
# Complexity O(2^n * n) if materializing subsets; cardinality is exactly 2^n.
