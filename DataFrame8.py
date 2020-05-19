import pandas as pd  
info = pd.DataFrame({'x': [2,4,5,4.2] ,'y': [5.3,4,3,5]  })  
hist = info.hist(bins=5) 
