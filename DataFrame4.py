import pandas as p
a1=p.DataFrame({"x":[23,45,32,44]})
a2=p.DataFrame({"x":[43,54,34]})
a3=a1.append(a2,ignore_index=True)
print(a3)
