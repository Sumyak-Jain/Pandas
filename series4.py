import pandas as pd
import numpy as np
x=pd.Series(data=[1,2,3,4])
y=pd.Series(data=[1.1,2.2,3.3,4.4],index=['a','b','c','d'])
print(x.index)
print(x.values)
print(y)
print(x.dtype)
print(y.itemsize)
print(y.shape)
print(y.ndim)
