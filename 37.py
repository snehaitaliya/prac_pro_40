#37.Write a Python program to replace missing values with zero.
import pandas as pd

data={'Name':['Shweta', 'Arohi', 'Bansi', 'Eshika', 'Charvi'],'Marks': [75,85,None,70,95]}
df=pd.DataFrame(data)
df=df.fillna(0)
print(df)