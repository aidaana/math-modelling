import numpy as np
import matplotlib.pyplot as plt
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
plt.rcParams['axes.grid']=True
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']

fig, ax = plt.subplots()

data_population = pd.read_excel('http://www.stat.kg/en/statistics/download/dynamic/314/')
base_year = 2011
population = np.array(data_population.loc[3].astype('str'))
real_pop = []
for i in population:
    if i[0].isdigit():
        real_pop.append(float(i))

f_0  = real_pop[0]
# k = growth rate
k = np.log(real_pop[10]/f_0)/10.0
def expo_f(t):
    return f_0 * np.exp(k * (t-base_year))

t = np.linspace(base_year, 2040, 150)
ax.plot(t, expo_f(t), color = "blue")

for i in range(base_year, base_year+len(real_pop)):
    ax.plot(i, real_pop[i-base_year], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")

ax.legend(['predicted exponential growth', 'real population in 2011-2022'])
plt.xlabel('Year')
plt.ylabel('Population')
string_title = "Exponential growth of male population in Kyrgyzstan"
plt.title(string_title)
plt.show()