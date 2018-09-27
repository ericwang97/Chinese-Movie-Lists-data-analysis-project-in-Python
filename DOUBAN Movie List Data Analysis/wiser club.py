import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
pd.options.mode.chained_assignment = None
import codecs
df1 = pd.ExcelFile("豆瓣·电影.xlsx") #读取数据
df = df1.parse('Sheet1')
print(df.shape)
print(df.info())
print(df.describe())

fig=plt.figure()
fig.set(alpha=0.65) # 设置图像透明度，无所谓
df['评分'].hist(bins = 100).plot(kind="bar")#分数的分布
plt.xlim(0,10)
plt.xlabel(u"score")# plots an axis lable
plt.ylabel(u"movie")
plt.title(u"distribution of score")


df.ix[df['上映年份'].isnull(),'上映年份'] = '2010'#处理缺失值，按平均值填充
df.ix[df['评价人数'].isnull(),'评价人数'] = 6319  #处理缺失值，按平均值填充
df.ix[df['评分'].isnull(),'评分'] = 7.2  #处理缺失值，按平均值填充
print(df.info())

fig.set(alpha=0.65)
df['评分'][df['评价人数'] >= 70000].plot(kind='kde',color='steelblue')
df['评分'][df['评价人数'] < 70000][df['评价人数'] >= 7000].plot(kind='kde',color='lightblue')
df['评分'][df['评价人数'] < 7000][df['评价人数'] >=700].plot(kind='kde',color='pink')
df['评分'][df['评价人数'] < 700].plot(kind='kde',color='red')
plt.legend((u'very famous(>70000 comments)', u'famous(7000-70000 comments)',u'medium(700-7000 comments)',u'low(<700 comments)'),loc='best') # sets our legend for our graph.
plt.xlim(0,10)
plt.xlabel(u"score")# plots an axis lable
plt.ylabel(u"probability")
plt.title(u"people & score")


fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.scatter(df['评价人数'], df['评分'])
plt.xlabel(u"people")# plots an axis lable
plt.ylabel(u"score")# plots an axis lable
plt.grid(b=True, which='major', axis='y')
plt.legend((u'distribution of comments'),loc='best')

cols = ["评分", "评价人数"]
df[cols].groupby('评分').mean().plot(kind='kde',color='lightblue')
plt.xlabel(u"people")# plots an axis lable
plt.grid(b=True, which='major', axis='y')
plt.legend((u'distribution of score'),loc='best')
plt.show()

df['评分'] = pd.cut(df['评分'], bins=10, labels=False)
fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.scatter(df['评价人数'], df['评分'])
plt.ylabel(u"movie")                         # 设定纵坐标名称
plt.xlabel(u"year")# plots an axis lable
plt.grid(b=True, which='major', axis='y')
plt.title(u"time & score")
plt.show()
#老片分数一般很集中在6-9分的中高分段，新片则两极分化愈发严重。


#下次解锁别的图？气泡图之类的？以及多维度的图。






