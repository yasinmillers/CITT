import numpy as np

import random

d_array= np.array([[23,45,43,23,45],[45,67,54,32,45]])
print(d_array[1,1])

list=[29,45,67,87,85,85,87]

def median1(n):
    y=np.median(list)
    return n + str(y)
print(median1("median is" ))

print((d_array > 45).sum())
print((d_array == 45).sum())
print((d_array < 45).sum())