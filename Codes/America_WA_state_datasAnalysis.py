
'''
https://github.com/theojulienne/covid-19-data/tree/master/data_collation/by_state/USA
'''

timeseries_dates = ["2020-01-22",
                    "2020-01-23",
                    "2020-01-24",
                    "2020-01-25",
                    "2020-01-26",
                    "2020-01-27",
                    "2020-01-28",
                    "2020-01-29",
                    "2020-01-30",
                    "2020-01-31",
                    "2020-02-01",
                    "2020-02-02",
                    "2020-02-03",
                    "2020-02-04",
                    "2020-02-05",
                    "2020-02-06",
                    "2020-02-07",
                    "2020-02-08",
                    "2020-02-09",
                    "2020-02-10",
                    "2020-02-11",
                    "2020-02-12",
                    "2020-02-13",
                    "2020-02-14",
                    "2020-02-15",
                    "2020-02-16",
                    "2020-02-17",
                    "2020-02-18",
                    "2020-02-19",
                    "2020-02-20",
                    "2020-02-21",
                    "2020-02-22",
                    "2020-02-23",
                    "2020-02-24",
                    "2020-02-25",
                    "2020-02-26",
                    "2020-02-27",
                    "2020-02-28",
                    "2020-02-29",
                    "2020-03-01",
                    "2020-03-02",
                    "2020-03-03",
                    "2020-03-04",
                    "2020-03-05",
                    "2020-03-06",
                    "2020-03-07",
                    "2020-03-08",
                    "2020-03-09",
                    "2020-03-10",
                    "2020-03-11",
                    "2020-03-12",
                    "2020-03-13",
                    "2020-03-14",
                    "2020-03-15",
                    "2020-03-16",
                    "2020-03-17",
                    "2020-03-18",
                    "2020-03-19",
                    "2020-03-20",
                    "2020-03-21",
                    "2020-03-22",
                    "2020-03-23",
                    "2020-03-24",
                    "2020-03-25",
                    "2020-03-26",
                    "2020-03-27",
                    "2020-03-28",
                    "2020-03-29",
                    "2020-03-30",
                    "2020-03-31",
                    "2020-04-01",
                    "2020-04-02",
                    "2020-04-03",
                    "2020-04-04",
                    "2020-04-05",
                    "2020-04-06",
                    "2020-04-07",
                    "2020-04-08",
                    "2020-04-09",
                    "2020-04-10",
                    "2020-04-11",
                    "2020-04-12",
                    "2020-04-13",
                    "2020-04-14",
                    "2020-04-15",
                    "2020-04-16",
                    "2020-04-17",
                    "2020-04-18",
                    "2020-04-19",
                    "2020-04-20",
                    "2020-04-21",
                    "2020-04-22",
                    "2020-04-23",
                    "2020-04-24",
                    "2020-04-25",
                    "2020-04-26",
                    "2020-04-27",
                    "2020-04-28",
                    "2020-04-29",
                    "2020-04-30",
                    "2020-05-01",
                    "2020-05-02",
                    "2020-05-03"
                    ]
total_confirmed = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    9,
    18,
    30,
    34,
    58,
    76,
    97,
    150,
    182,
    249,
    349,
    397,
    481,
    551,
    702,
    806,
    939,
    1067,
    1240,
    1414,
    1563,
    1804,
    2042,
    2284,
    2496,
    2877,
    3339,
    3822,
    4305,
    4737,
    5121,
    5589,
    6049,
    6540,
    6893,
    7424,
    7792,
    8181,
    8523,
    8859,
    9214,
    9492,
    9941,
    10162,
    10398,
    10587,
    10789,
    11100,
    11343,
    11673,
    11887,
    12146,
    12346,
    12550,
    12785,
    12995,
    13297,
    13521,
    13521,
    13521,
    13686,
    13842,
    14070,
    14327,
    14637,
    15003
]

total_death = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    2,
    2,
    4,
    5,
    8,
    11,
    14,
    16,
    20,
    26,
    27,
    31,
    35,
    37,
    40,
    44,
    47,
    51,
    57,
    69,
    78,
    82,
    92,
    104,
    111,
    126,
    137,
    146,
    159,
    183,
    199,
    220,
    237,
    248,
    262,
    282,
    310,
    338,
    365,
    386,
    407,
    429,
    443,
    459,
    476,
    494,
    509,
    526,
    542,
    551,
    571,
    585,
    598,
    615,
    629,
    640,
    647,
    654,
    659,
    665,
    738,
    749,
    765,
    786,
    801,
    814,
    824,
    830
]
total_suspected = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    9,
    41,
    111,
    263,
    485,
    707,
    1040,
    1528,
    1994,
    2517,
    3522,
    5247,
    7458,
    11122,
    15300,
    17589,
    19311,
    24047,
    28608,
    33256,
    37623,
    41632,
    43978,
    45924,
    50988,
    56218,
    61268,
    65809,
    70192,
    72939,
    74909,
    79847,
    84433,
    89097,
    93782,
    98608,
    101321,
    103467,
    108360,
    113370,
    118061,
    122036,
    126337,
    128398,
    129931,
    133868,
    137898,
    141928,
    146094,
    150444,
    152696,
    154354,
    158765,
    163567,
    167964,
    171631,
    174830,
    175440,
    175440,
    175477,
    179679,
    182515,
    187800,
    193981,
    198724,
    207315
]

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
fig,ax = plt.subplots(nrows=1,ncols=1,figsize = (20,8))
ax.plot(timeseries_dates,total_confirmed,'b--',linewidth = 1,label = '总确诊人数')
ax.plot(timeseries_dates,total_suspected,'g--',linewidth = 1,label = '总疑似人数')
ax.plot(timeseries_dates,total_death,'r--',linewidth = 1,label = '总死亡人数')

ax.set_yticks(range(0,220000,10000))
ax.set_xticks(list(range(0,len(timeseries_dates),4)))
ax.set_xticklabels([timeseries_dates[i] for i in list(range(0,len(timeseries_dates),4))],rotation = 45)
plt.legend(loc='upper left',fontsize=15)
plt.ylabel('人数（/人）',fontsize=16)
plt.grid()
plt.title('美国WA州疫情数据变化')
plt.savefig('D:\\Python\\数学建模大作业\\pictures\\WA.png',dpi = 180)
plt.show()
