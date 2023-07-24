import pandas as pd
import jieba.analyse
import matplotlib.pyplot as plt
data = pd.read_csv('days/12_15.csv', header = None,encoding = 'utf-8-sig')
title = data.iloc[:,0] # 获得第一列
Title = title.values
flag = 0
str = Title[0]
for item in Title:
    if(flag == 0):
        flag = 1
        continue
    str += item

jieba.suggest_freq('车保罗', True)
jieba.suggest_freq('姆巴佩', True)
words = jieba.lcut(str)
word_dict = {}
for word in words:
        if len(word) == 1: # 如果关键字字数为1，不统计; 否则加1
            continue
        else:
            word_dict[word] = word_dict.get(word, 0) + 1
word_zip = zip(word_dict.values(), word_dict.keys())
word_sort = list(sorted(word_zip, reverse = True))# 对元组里面的元素按照value从大到小进行排序
df = pd.DataFrame(list(word_sort))
#print(df.iloc[:20, 1])
count = df.iloc[:20, 0]
name = df.iloc[:20, 1]
plt.bar(range(20),count,tick_label = name)
for x, y in enumerate(list(count)):
    plt.text(x, y+1, '%s' % y, ha = 'center')
plt.rcParams['font.sans-serif'] = ['SimHei'] # 中文设置为黑体
plt.xticks(rotation = 30) # x轴标签旋转30度
plt.title("12-15")
plt.tight_layout()
plt.show()