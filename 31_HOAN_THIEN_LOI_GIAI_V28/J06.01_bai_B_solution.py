import dis

def by_loop(xs):
    out=[]
    for x in xs: out.append(x*x)
    return out

def by_comp(xs): return [x*x for x in xs]
assert by_loop([1,2,-3])==by_comp([1,2,-3])
op1=[i.opname for i in dis.get_instructions(by_loop)]
op2=[i.opname for i in dis.get_instructions(by_comp)]
assert op1 and op2
# Do not lock a test to specific opcode names; opcode spelling changes across releases.
