#Write a Python program to find students who scored more than 80 marks using Pandas.
import pandas as pd

data={'Name':['Shweta', 'Arohi', 'Bansi', 'Eshika', 'Charvi'],'Marks': [75, 85, 90, 70, 95]}

df=pd.DataFrame(data)
df=df[df['Marks'] > 80]
print(df)