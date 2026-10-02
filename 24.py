#Write a Python program to insert an element at a specified position in an array.
import numpy as np

l=np.array([12,45,67,32,78])
new=10
pos=3
n=len(l)                   
l=np.insert(l,pos,new)
print(l)

