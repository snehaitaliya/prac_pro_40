#Write a Python program to replace all even numbers in an array with zero.
import numpy as np
l=np.array([1,2,3,4,5,6,7,8,9,10])
l[l%2==0]=0
print(l)