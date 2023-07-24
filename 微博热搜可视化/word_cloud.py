import pandas as pd
import jieba.analyse
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from matplotlib import colors
data = pd.read_csv('days/12_20.csv', header = None, encoding = 'utf-8-sig')
title = data.iloc[:,0] # 获得第一列
Title = title.values
#print(Title)
# 做词云不去重
flag = 0
str = Title[0]
for item in Title:
    if(flag == 0):
        flag = 1
        continue
    str += item
    #print(str)
    #break
jieba.suggest_freq('奥密克戎', True)
jieba.suggest_freq('连花清瘟', True)
jieba.suggest_freq('吞刀片', True)
jieba.suggest_freq('咽口水', True)
jieba.suggest_freq('C罗', True)
jieba.suggest_freq('发不雅信息', True)
jieba.suggest_freq('川渝', True)
jieba.suggest_freq('想见你', True)
jieba.suggest_freq('黄子韬', True)
jieba.suggest_freq('新冠', True)
jieba.suggest_freq('撸下口罩', True)
jieba.suggest_freq('姆巴佩', True)
jieba.suggest_freq('涮肉', True)
jieba.suggest_freq(('瘟', '能'), True)
jieba.suggest_freq(('瘟', '一次'), True)
jieba.suggest_freq(('期', '杀'), True)
words = " ".join(jieba.cut(str))
color_list = ['#CD0000', '#CD3700', '#CD4F39', '#CD5B45', '#CD6600', '#CD8500', '#CD8162', '#CD7054', '#CD3333', '#CD2626', '#CD661D', '#CD853F', '#CDBA96', '#CDAA7D', '#CD6839', '#CD5555', '#CD9B9B', '#CD950C', '#CD9B1D', '#CDAD00', '#CDCD00', '#CDCDB4', '#CDBE70', '#CDC673', '#A2CD5A', '#9ACD32', '#66CD00', '#00CD00', '#00CD66', '#7CCD7C', '#43CD80', '#9BCD9B', '#66CDAA', '#79CDCD', '#00CDCD', '#00C5CD', '#7AC5CD', '#96CDCD', '#EE0000', '#EE4000', '#EE5C42', '#EE6A50', '#EE7600', '#EE9A00', '#EE9572', '#EE8262', '#EE3B3B', '#EE2C2C', '#EE7621', '#EE9A49', '#EED8AE', '#EEC591', '#EE7942', '#EE6363', '#EEB4B4', '#EEAD0E', '#EEB422', '#EEC900', '#EEEE00', '#EEEED1', '#EEDC82', '#EEE685', '#BCEE68', '#B3EE3A', '#76EE00', '#00EE00', '#00EE76', '#90EE90', '#4EEE94', '#B4EEB4', '#76EEC6', '#8DEEEE', '#00EEEE', '#00E5EE', '#8EE5EE', '#AEEEEE', '#FF0000', '#FF4500', '#FF6347', '#FF7256', '#FF7F00', '#FFA500', '#FFA07A', '#FF8C69', '#FF4040', '#FF3030', '#FF7F24', '#FFA54F', '#FFE7BA', '#FFD39B', '#FF8247', '#FF6A6A', '#FFC1C1', '#FFB90F', '#FFC125', '#FFD700', '#FFFF00', '#FFFFE0', '#FFEC8B', '#FFF68F', '#CAFF70', '#C0FF3E', '#7FFF00', '#00FF00', '#00FF7F', '#9AFF9A', '#54FF9F', '#C1FFC1', '#7FFFD4', '#97FFFF', '#00FFFF', '#00F5FF', '#98F5FF', '#BBFFFF', '#8B0000', '#8B2500', '#8B3626', '#8B3E2F', '#8B4500', '#8B5A00', '#8B5742', '#8B4C39', '#8B2323', '#8B1A1A', '#8B4513', '#8B5A2B', '#8B7E66', '#8B7355', '#8B4726', '#8B3A3A', '#8B6969', '#8B658B', '#8B6914', '#8B7500', '#8B8B00', '#8B8B7A', '#8B814C', '#8B864E', '#6E8B3D', '#698B22', '#008B00', '#458B00', '#008B45', '#548B54', '#2E8B57', '#698B69', '#458B74', '#528B8B', '#008B8B', '#00868B', '#53868B', '#668B8B']
colormap = colors.ListedColormap(color_list) # 将自定义的色号转化为wc可用的colormap
icon = np.array(Image.open('icon.jpg'))
word_cloud = WordCloud(
        scale = 8,
        font_path = 'C:/Windows/Fonts/STXINWEI.TTF', # 显示中文需要加载本地中文字体
        background_color = '#383838',
        colormap = colormap,
        prefer_horizontal = 0.8, # 水平显示的文字相对于竖直显示文字的比例
        mask = icon, # 添加蒙版
        relative_scaling = 0.3, # 设置字体大小与词频的关联程度为0.3
        max_font_size = 80, # 设置显示的最大字体
        stopwords = {'岁','的', '是', '吗', '和', '了', '被', '你', '这', '能', '至今', '颗',
                     '怎么', '对', '已', '称有', 'VS', '成', '都', '有', '多', '还', '一起',
                     '不戴', '我', '比', '贴', '层涨', '元', '摔', '条', '上', '千元', '还有',
                     '卖', '到', '应', '后', '戴', '买', '吃', '天', '与', '却', '真的', '又',
                     '不', '将', '宣布', '当定', '一盒', '会', '粒', '买块', '患', '嫌', '要',
                     '点', '让', '一板', '只', '第', '再', '种', '什么', '一支', '不了', '千',
                     '天内', '知道', '不到', '个', '为何', '才', '遇人', '或超', '薇给', '超', 
                     '给', '病', '因', '万买', '冠', '半', '一次', '它在', '想', '称', '穿', '疯',
                     '度', '就', '在', '从', '摊', '它', '差点', '囤', '号', '叫', '全是', '带到',
                     '为什么', '像', '是因为', '有人', '开', '时', '月', '轮', '斤', '小时', '造',
                     '毛', '么', '她', '前', '年', '不是', '瘟', '称此', '做好', '哪', '我们',
                     '例', '花', '把', '期间', '当回事', '如何', '增', '他们', '带来', '人', '期',
                     '杀', '帮', '引', '或', '一', '名', '秒', '可', '写', '也', '没', ' 几乎',
                     '地', '变', '忍住', '取决于'})
word_cloud.generate(words)
word_cloud.to_file('t6.jpg')