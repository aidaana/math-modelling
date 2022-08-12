import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 12
plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['image.interpolation'] = 'none'
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['axes.grid'] = True
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 8

def f(t, f0, a, s, h):
    return f0 * np.exp(a * t) + (s - h) * (np.exp(a * t) - 1) / a

f0 = float(input("Enter initial value of a quantity: "))
a = float(input("Enter growth rate: "))
s = float(input("Enter the stocking rate: "))
h = int(input("Enter the harvesting rate: "))

fig, ax = plt.subplots()
t = np.linspace(0, 100, 1000)
ax.plot(t, f(t, f0, a, s, h), color = "blue")

# for i in range(n+1):
#     ax.plot(t[i], y[i], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")

ax.legend(['exponential'])
titleString = 'The growth with initial quantity = %.3f, the growth rate = %.3f, stocking rate = %d, harvesting rate = %d' % (f0, a, s, h)
plt.title(titleString)
plt.ylabel("quantity")
plt.xlabel("time")
plt.show()







