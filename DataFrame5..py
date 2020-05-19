import pandas as p
a1=p.DataFrame({"x":[23,45,32,44],"y":[43,54,34,45]})
a2=a1.agg(['sum','min','max'])
print(a1)
print(a2)
