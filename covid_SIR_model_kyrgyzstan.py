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


# number of days inspected
n = 211
time = []
for i in range(n):
    time.append(i)

# population inspected out of 6.5 mln
population = 100000

# data from https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv  57th day
infected = [3,3,6,14,14,16,42,44,44,58,58,84,94,107,111,116,130,144,147,216,228,270,280,298,339,377,419,430,449,466,489,506,554,568,590,612,631,665,665,682,695,708,729,746,756,769,795,830,843,871,895,906,931,1002,1016,1037,1044,1082,1111,1117,1138,1216,1243,1270,1313,1350,1365,1403,1433,1468,1520,1594,1662,1722,1748,1817,1845,1871,1899,1936,1974,2007,2032,2055,2093,2166,2166,2207,2285,2472,2562,2657,2657,2789,2981,3356,3356,3726,3954,4204,4446,4513,5017,5296,5506,6261,6767,6878,7094,7377,8141,8279,8847,9358,9910,10410,11117,11444,11444,12282,12498,13101,24606,27143,27143,28251,28980,31247,31247,32124,32813,33296,33844,34592,35223,35805,36299,36719,37129,37541,38110,38659,39162,39571,39919,40085,40455,40759,41069,41373,41645,41856,41991,42146,42325,42507,42703,42889,43023,43126,43245,43358,43459,43587,43712,43820,43898,43958,44036,44135,44199,44293,44403,44458,44487,44613,44684,44761,44828,44881,44928,44999,45072,45153,45244,45335,45335,45471,45542,45630,45757,45932,46090,46251,46355,46522,46669,46841,47056,47184,47428,47635,47799,48097,48342,48617,48924,49230,49528,49871,50201]

susceptible = []
for i in range(n):
    susceptible.append(population-infected[i])

# data from https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv
recovered = [0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,5,6,9,9,33,33,33,35,35,44,54,67,71,78,91,114,130,133,201,216,254,302,345,345,370,395,416,437,462,504,527,564,575,600,614,637,650,658,675,688,709,726,735,745,783,804,827,898,910,923,939,957,980,992,1015,1043,1066,1088,1113,1170,1181,1219,1265,1292,1340,1360,1425,1445,1483,1572,1668,1668,1722,1791,1847,1902,1933,1933,1961,1981,2021,2021,2082,2112,2162,2194,2212,2294,2370,2443,2530,2655,2671,2714,2802,2916,2967,3053,3134,3236,3253,3460,3538,3538,3712,3735,3821,10704,13109,13109,14776,15536,18038,18038,19203,20388,21205,22296,22296,23985,25037,26419,27274,27927,28743,29513,30099,30764,31062,31822,32126,32734,32997,33288,33592,33951,34276,34537,34855,35197,35486,35831,36056,36397,36615,36925,37217,37492,37726,37973,38198,38459,38649,38895,39174,39389,39599,39826,39960,40092,40336,40487,40631,40779,40922,41023,41103,41210,41317,41415,41484,41484,41682,41796,41904,42005,42147,42302,42453,42613,42761,42879,42983,43137,43278,43418,43521,43644,43798,43957,44097,44227,44227,44522,44712,44884]
# data from https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
deaths = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,4,4,4,4,5,5,5,5,5,5,5,5,5,5,7,7,7,8,8,8,8,8,8,8,8,8,8,10,10,11,12,12,12,12,12,12,12,12,12,14,14,14,14,14,14,14,14,14,14,16,16,16,16,16,16,16,16,17,20,20,22,22,22,23,24,26,26,26,27,27,28,30,31,31,32,35,40,40,42,43,43,46,46,50,57,61,66,76,76,78,88,99,107,116,122,125,129,147,149,149,165,167,173,900,1037,1037,1079,1111,1211,1211,1249,1277,1301,1329,1347,1364,1378,1397,1409,1420,1427,1438,1447,1451,1459,1468,1474,1478,1484,1487,1491,1493,1495,1496,1498,1498,1498,1055,1055,1056,1057,1057,1057,1057,1057,1057,1058,1058,1059,1059,1059,1060,1060,1060,1060,1060,1061,1061,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1063,1064,1064,1064,1065,1065,1066,1066,1066,1066,1069,1073,1077,1082,1085,1090,1092,1094]

removed = []
for i in range(n):
    removed.append(recovered[i] + deaths[i])

for i in range(n):
    infected[i] = infected[i] - removed[i]

# parameters for SIR model
beta = 0.17
gamma = 0.10

# for susceptoble population
def dsdt(s, i):
    return -beta * s * i/100000

# for infected population
def didt(s, i):
    return (beta * s * i/100000 - gamma * i)

# initial values for runge-kutta4 method, that solves a system of 2 equations: dsdt, didt
susceptibleSIR = [population-infected[0]]
infectedSIR = [infected[0]]
def rungekutta(s0, i0, n, h):
    for i in range(1,n):
        sk1 = dsdt(s0, i0)
        ik1 = didt(s0, i0)

        sk2 = dsdt(s0 + h/2*sk1, i0 + h/2*ik1)
        ik2 = didt(s0 + h/2*sk1, i0 + h/2*ik1)

        sk3 = dsdt(s0 + h/2 * sk2, i0 + h/2*ik2)
        ik3 = didt(s0 + h / 2 * sk2, i0 + h / 2 * ik2)

        sk4 = dsdt(s0 + h * sk3, i0 + h * ik3)
        ik4 = didt(s0 + h * sk3, i0 + h * ik3)

        s0 = s0 + h/6*(sk1 + 2*sk2 + 2*sk3 + sk4)
        i0 = i0 + h / 6 * (ik1 + 2 * ik2 + 2 * ik3 + ik4)
        susceptibleSIR.append(s0)
        infectedSIR.append(i0)

rungekutta(susceptibleSIR[0],infectedSIR[0],n,1.0)

removedSIR = []
for i in range(n):
    removedSIR.append(population-susceptibleSIR[i]-infectedSIR[i])

fig, ax = plt.subplots()
ax.plot(time, susceptible, color = 'xkcd:cadet blue')
ax.plot(time, infected, color = 'orange')
ax.plot(time, removed, color = 'xkcd:sage green')

ax.plot(time, susceptibleSIR, color = 'xkcd:dark blue')
ax.plot(time, infectedSIR, color = 'xkcd:dark orange')
ax.plot(time, removedSIR, color = 'green')

# adjust time-axis to months
x = [14, 44, 75, 105, 136, 167, 197]
labels = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
plt.xticks(x, labels, rotation = 45)

ax.legend(['actual susceptible', 'actual infected', 'actual removed', 'approx. susceptible', 'approx. infected', 'approx. removed'])
titleString = 'Covid-19 in Kyrgyzstan 2020: actual data vs. SIR model'
plt.title(titleString)
plt.ylabel("cases")
plt.xlabel("2020")
plt.show()


