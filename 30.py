#Write a Python program to shuffle the elements of an array.
import numpy as np
l=np.array([1,2,3,4,5,6,7,8,9,10])
np.random.shuffle(l)
print(l)