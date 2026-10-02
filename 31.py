#Write a Python program to generate a random password using NumPy.
import numpy as np
length = 10
char=np.array(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"))
password=''.join(np.random.choice(char,size=length))
print(password)