# On empty domain: forall(P) is True; exists(P) is False.
xs=[]
assert all(x>0 for x in xs) is True
assert any(x>0 for x in xs) is False
xs=[1,2,3]
assert all(x>0 for x in xs)
assert any(x==2 for x in xs)
assert not any(x<0 for x in xs)
