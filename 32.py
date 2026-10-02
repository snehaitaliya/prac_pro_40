#Write a Python program to replace missing (NaN) values with the mean of the array.
import numpy as np
l=np.array([1,2,np.nan,4,5])
l[np.isnan(l)]=np.nanmean(l)
print(l)