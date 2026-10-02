#38.Write a Python program to find the mean, median, and mode of DataFrame columns.

import pandas as pd

data={'Name':['Shweta', 'Arohi', 'Bansi', 'Eshika', 'Charvi'],'Marks': [75, 85, 90, 70, 95]}

df=pd.DataFrame(data)
print("Mean: ",df['Marks'].mean())
print("Median: ",df['Marks'].median())
print("Mode: ",df['Marks'].mode())

