import numpy as np
student_scores = [80,72,35,48,55,98,90,85,70,66,54,40,84,60,90,50,66,67,30]


def class_exam(args):
    percent = np.percentile(student_scores,70)
    return args + str(percent)
print(class_exam("Students that scored under a 70: "))

#2.
arr = np.array([1,2,3,4,5,6],ndmin = 6)


print(np.transpose([arr]))

arr2 = np.array([[[[[[[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]]]]]]])


print(arr2)
print(arr2.reshape(2,8))


x = np.array([20,40,7,80,100,200])

y = np.array([100,70,10,22,41,55])


z = np.multiply(x,y)

print(z)
print(z.reshape(6,1))
