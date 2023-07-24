from snownlp import SnowNLP
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def clean(f_1):
    f_1 = f_1.dropna()
    f_1 = f_1.reset_index()
    f_1.drop(f_1.tail(50).index, inplace = True)
    return f_1

f_1 = pd.read_csv('days/12_15.csv', header = None, encoding = 'utf-8-sig')
f_2 = pd.read_csv('days/12_16.csv', header = None, encoding = 'utf-8-sig')
f_3 = pd.read_csv('days/12_17.csv', header = None, encoding = 'utf-8-sig')
f_4 = pd.read_csv('days/12_18.csv', header = None, encoding = 'utf-8-sig')
f_5 = pd.read_csv('days/12_19.csv', header = None, encoding = 'utf-8-sig')
f_6 = pd.read_csv('days/12_20.csv', header = None, encoding = 'utf-8-sig')
f_7 = pd.read_csv('days/12_21.csv', header = None, encoding = 'utf-8-sig')

#l = [f_1, f_2, f_3, f_4, f_5, f_6, f_7]
#data = pd.concat(l)
#print("处理前: %d条" % data.shape[0])

f_1 = clean(f_1)
f_2 = clean(f_2)
f_3 = clean(f_3)
f_4 = clean(f_4)
f_5 = clean(f_5)
f_6 = clean(f_6)
f_7 = clean(f_7)
l = [f_1, f_2, f_3, f_4, f_5, f_6, f_7]
data = pd.concat(l)
#print("处理后: %d条" % data.shape[0])
#data = pd.read_csv('days12_21.csv', header = None,encoding = 'utf-8-sig')
#print("处理前: %d条" % data.shape[0])
#data = data.dropna()
#data = data.reset_index()
#data.drop([len(data) - 50], inplace = True)
#data.drop(data.tail(50).index, inplace = True) # 从尾部去掉n行
#print("处理后: %d条" % data.shape[0])
#print(data.iloc[0, 5].split()[1])
time = []
for i in range(0, len(data), 300): # 每隔50行取数据 /300 /4250 (every 10min/ 1h/ 1day)
    date = data.iloc[i, 5].split()[1] #split()[1]
    time.append(date)
#print(time)
title = data.iloc[:,1] # 获得第一列
#print(title.values)
Title = title.values
#Title[0] = eval(Title[0])
#print(Title)
flag = 0
score = []
temp = []
for topic in Title:
    #print(topic)
    s = SnowNLP(topic)
    temp.append(s.sentiments)
    flag += 1
    if flag == 300:
        flag = 0
        avg = np.mean(temp)
        score.append(avg)
        temp = []

x = range(98) # x = range(7)
x = list(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x = x, y = score))
fig.update_layout(title = 'every hour in 7 days', xaxis = dict( tickmode = 'array', tickvals = x,
                                ticktext = time))
fig.update_xaxes(rangeslider_visible = True, title = {'text': 'Time'})
fig.update_yaxes(title = {'text': 'Score'})
fig.add_trace(go.Scatter(x = [7, 21, 35, 49, 63, 77, 91],
                 y = [0.715, 0.715, 0.715, 0.715, 0.715, 0.715, 0.715], line_dash = 'dash',
                 text = ['12-15', '12-16', '12-17', '12-18', '12-19', '12-20', '12-21'],
                 mode = 'text'))
for i in range(6):
    i += 1
    fig.add_vline(x = 14*i, line_dash = 'dash')
fig.show()