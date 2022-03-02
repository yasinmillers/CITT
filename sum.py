import numpy as np
import random

"""
newarr1 = np.array([[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0]])
newarr2 = np.array([[10.0,11.0,12.0,13.0],[14.0,15.0,16.0,17.0]])

print(np.divide(newarr1,newarr2))
"""

top_players = [23.1,29.2,26.5,28,29.1,32.2]


#The average players dont average more than 32.2 points
def player_percentage(args):
    percentage = np.percentile(top_players,100)
    return args + str(percentage)
print(player_percentage("Players averaging lower than 24 pts is: "))



x = np.array([12,14,3,44,33,22,333,44,9,6,101])
y = np.array([20,12,55,100,4,56,70,9,10,3,101])

z = np.vstack((x,y))
w = np.hstack((x,y))



print(z)
print(w)
print(z.sum())

print((100 > x).sum())

p = x*y

print(p.shape)
# print(p.reshape(2,5))


print(p[3]*p[4])

print(np.ndim(p))

# print(p.reshape(2,5))

print(np.vstack(p))

e = np.linspace(12,100)
f = np.arange(10,100)

print(e)
print(f)

arr3 = np.linspace(1,100,5)#Start,Stop,Num
arr4 = np.arange(1,100,5)#Start,Stop,Go(The amount of steps)

print(arr3)
print(arr4)

