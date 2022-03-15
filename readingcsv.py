import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

font1 = {'family': 'serif',
         'color':  'red',
         'weight': 'normal',
         'size': 20, }

data = pd.read_csv('data.csv', skiprows=3)
# print(data)
# print(data.info)
# data.plot(kind='bar')
# plt.title('New Cases', fontdict=font1)
# plt.show()

print(data)
print(data.info)

data.plot(kind='bar')
plt.title("Covid Data", fontdict=font1)
plt.show()
