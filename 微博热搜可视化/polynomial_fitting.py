import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f_1 = pd.read_csv('D:/code/days/12_15.csv', header = None, encoding = 'utf-8-sig')
f_2 = pd.read_csv('D:/code/days/12_16.csv', header = None, encoding = 'utf-8-sig')
f_3 = pd.read_csv('D:/code/days/12_17.csv', header = None, encoding = 'utf-8-sig')
f_4 = pd.read_csv('D:/code/days/12_18.csv', header = None, encoding = 'utf-8-sig')
f_5 = pd.read_csv('D:/code/days/12_19.csv', header = None, encoding = 'utf-8-sig')
f_6 = pd.read_csv('D:/code/days/12_20.csv', header = None, encoding = 'utf-8-sig')
f_7 = pd.read_csv('D:/code/days/12_21.csv', header = None, encoding = 'utf-8-sig')
l = [f_1, f_2, f_3, f_4, f_5, f_6, f_7]
data = pd.concat(l)
data = data.dropna()
#print(data.iloc[:, 0].value_counts())
# print(data.shape[0])
# print(data[data.iloc[:, 0] == '考研'][2].values)
x = range(179)
x = np.array(x)
y = data[data.iloc[:, 0] == '考研'][2].values
z1 = np.polyfit(x, y, 70)
p1 = np.poly1d(z1)
# 求对应x的各项拟合函数值
fx = p1(x)
# 绘制坐标系散点数据及拟合曲线图
plot1 = plt.plot(x, y, label = 'origin data')
plot2 = plt.plot(x, fx, 'r', label = 'polyfit data')
plt.xlabel('提及次数')
plt.ylabel('热度')
plt.rcParams['font.sans-serif'] = ['SimHei'] # 中文设置为黑体
plt.show()