def prefix_sum(values):
    total=0
    for i,x in enumerate(values):
        # Invariant at start of iteration i: total == sum(values[:i]).
        assert total==sum(values[:i])
        total+=x
    assert total==sum(values)
    return total
assert prefix_sum([1,-4,5])==2
assert prefix_sum([])==0
# Proof: initial total=0; each step adds values[i]; on termination total=sum(values).
