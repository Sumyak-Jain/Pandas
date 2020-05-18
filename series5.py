import pandas as pd    
a = pd.Series(['Java', 'C', 'C++'])  
b=a.map('i like {}'.format, na_action='ignore')
print(a)
print(b)
