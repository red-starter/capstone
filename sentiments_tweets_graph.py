import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import pandas as pd
import numpy as np
from pandas_datareader import data

df = pd.read_json('sentiments_day_tweets.json')

df.to_csv('all_days.csv')
# df.drop(df.columns[[1,3]], axis=1, inplace=True)
N = len(df.columns)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure(figsize=(100, 100))
ax = fig.add_subplot(111)

yvals =  df.iloc[0]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals =  df.iloc[1]
rects2 = ax.bar(ind+width, zvals, width, color='b')
kvals =  df.iloc[2]
rects3 = ax.bar(ind+width*2, kvals, width, color='g')

ax.set_ylabel('Frequency')
ax.set_xticks(ind+width)

cols = list(map(lambda x: str(x)[:10],df.columns))
ax.set_xticklabels(cols)
ax.legend( (rects1[0], rects2[0], rects3[0]), ('negative', 'neutral', 'positive') )

# def autolabel(rects):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.02*h, '%d'%int(h),
#                 ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
ax.tick_params(axis='x', labelrotation=90)
plt.show()