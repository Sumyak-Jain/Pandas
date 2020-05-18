import pandas as pd    
a = pd.Series(["gaurav","jain"],name="names")
b=a.to_frame()
print(b)
