import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

x = np.array([10, 15, 20, 25, 100, 35, 40, 45])
y = np.array([100, 10, 120, 130, 140, 150, 160, 170])

font1 = {
    "family": "serif",
    "color": "red",
    "size": 20
}

font2 = {
    "family": "serif",
    "color": "yellow",
    "size": 15
}

font3 = {
    "family": "serif",
    "color": "blue",
    "size": 15
}

plt.title("News Channel Data", fontdict=font1)
plt.xlabel("X Data", fontdict=font2)
plt.ylabel("Y data", fontdict=font3)

plt.plot(x, y, color="yellow", marker=">")
plt.grid()
plt.show()

x1 = np.random.randint(100, size=(100))
y1 = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x1, y1, c=colors, s=sizes, cmap="flag", alpha=0.5)
plt.title("Random Color Graph", fontdict=font1)

plt.colorbar()

plt.show()
