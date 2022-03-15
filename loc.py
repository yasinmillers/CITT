import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


car_sales = {
    "bmw": [2000, 4000, 66000, 78000, 100000],
    "lambo": [15000, 30000, 50000, 70000, 100000],
    "nissan": [10000, 20000, 40000, 60000, 80000],
    "harrier": [5000, 10000, 20000, 30000, 40000]

}
dates = pd.date_range('15/3/2022', periods=5, )
data = pd.DataFrame(car_sales, index=dates)
print(data)
