#36.Write a Python program to remove duplicate records from a DataFrame.

import pandas as pd
data={'Name':['Shweta', 'Arohi', 'Bansi', 'Eshika', 'Charvi','Shweta'],'Marks': [75, 85, 90, 70, 95,75]}
df=pd.DataFrame(data)
df=df.drop_duplicates()
print(df)