import statistics
xs=[1.0,1.1,1.2,1.3,1.4,1.5,1.1,1.0,1.2,9.0]
quartiles=statistics.quantiles(xs,n=4,method='inclusive')
iqr=quartiles[2]-quartiles[0];median=statistics.median(xs)
assert iqr>0 and median<2
outliers=[x for x in xs if x>quartiles[2]+1.5*iqr]
assert outliers==[9.0]
