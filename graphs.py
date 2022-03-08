import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


#1.
                #c     #0                       #1
arr = np.array([[40,90,140,220,330,400],[510,520,530,540,550,560]])
            #position 0,1,2,3,4,5

print(arr[1,3:])

#2.
company_data = [100,2,33,45,66,7,8,9,9990,33,22,333,4,89,19,
                20,55,7,90,1000,40,70,20,33,55,500,60,444,99]
#3.
x = np.array([20,30,40,50,60,70,80,90,100])
y = np.array([120,130,140,150,160,170,180,190,200])


plt.plot(x,y)
plt.show()
#4.
arr1 = np.array([[40,90,140,220,330,400],[510,520,530,540,550,560]])

print(arr1[0]*arr1[1])

#5.
arr3 = [90,22,70,17,8,37,10,2,55,9]

arr4 = np.arange(0,10,1)

def selectionsort(num):
    for i in range(len(num)):
        midindex = i
        for j in range(i+1,len(num)):
            plt.bar(arr4,arr3)
            plt.pause(0.05)
            plt.clf()
            if arr3[j] < arr3[midindex]:
                midindex = j
        arr3[i],arr3[midindex] = arr3[midindex],arr3[i]

selectionsort(arr3)
plt.show()
