#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import pandas as pd
import numpy as np



df = pd.read_json('sentiments_day_tweets.json')

N = len(df.columns)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure(figsize=(100, 100))
ax = fig.add_subplot(111)

yvals =  df.iloc[0]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals =  df.iloc[1]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals =  df.iloc[2]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Frequency', fontsize=40)
ax.set_xticks(ind+width)

cols = list(map(lambda x: str(x)[:10],df.columns))
ax.set_xticklabels(cols, fontsize=100)
ax.legend( (rects1[0], rects2[0], rects3[0]), ('negative', 'neutral', 'positive') , fontsize=100)

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*h, '%d'%int(h),
                ha='center', va='bottom',fontsize=40)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
ax.tick_params(axis='x', labelrotation=90)
ax.yaxis.label.set_size(100)
ax.xaxis.label.set_size(100)











x = np.random.randn(1000, 3)



x





