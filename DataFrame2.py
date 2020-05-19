import pandas as pd
a1={"names":["gaurav","sumyak"],"age":[19,20]}
a=pd.DataFrame(a1)

print(a)
del a["age"]
print(a)

#same way addition of column can also be done
