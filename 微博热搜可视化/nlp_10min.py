from snownlp import SnowNLP
import pandas as pd

import plotly.express as px
import numpy as np

data = pd.read_csv('days/12_15.csv', header = None, encoding = 'utf-8-sig')
#print("处理前: %d条" % data.shape[0])
data = data.dropna()
#print("剔除热度为0后: %d条" % data.shape[0])
time = []
for i in range(0, len(data), 50): # 每隔50行取数据
    date = data.iloc[i, 4].split()[1]
    time.append(date)
#print(len(time))
title = data.iloc[:,0] # 获得第一列
#print(title.values)
Title = title.values
#Title[0] = eval(Title[0])
flag = 0
score = []
temp = []
for topic in Title:
    #print(topic)
    s = SnowNLP(topic)
    temp.append(s.sentiments)
    #score.append(s.sentiments)
    flag += 1
    if flag == 50:
        flag = 0
        avg = np.mean(temp)
        score.append(avg)
        temp = []

x = range(85)
x = list(x)
#print(len(score))

fig = px.line(x = x, y = score)
fig.update_layout(title = 'every 10min on 12-21',xaxis = dict( tickmode = 'array', tickvals = x,
                                ticktext = time))
fig.update_xaxes(rangeslider_visible = True, title = {'text': 'Time'})
fig.update_yaxes(title = {'text': 'Score'})
fig.show()
