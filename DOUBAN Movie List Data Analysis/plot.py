import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
pd.options.mode.chained_assignment = None
import codecs
df = pd.read_csv("score.csv") #读取数据
print(df.shape)
print(df.info())
print(df.describe())
print(pd.crosstab(df.time, df.score))
fig=plt.figure()



#画图
fig.set(alpha=0.65) # 设置图像透明度，无所谓
df.score.hist(bins = 100).plot(kind="bar")#分数的分布
plt.xlim(0,10)
plt.xlabel(u"score")# plots an axis lable
plt.ylabel(u"movie")
plt.title(u"distribution of score")
plt.show()
plt.savefig('distribution of score.png')   # 保存图片
#了解分数的分布。当然这一点describe里也有


fig.set(alpha=0.35) # 设置图像透明度，无所谓
df.time.hist(bins = 102).plot()#分数的分布
plt.xlabel(u"year")# plots an axis lable
plt.title(u"distribution of year") # 标题
plt.ylabel(u"movie")
plt.grid(b=True, which='major', axis='y')
plt.show()
plt.savefig('distribution of year.png')   # 保存图片
#了解电影制造年份的分布。同理describe就有




fig.set(alpha=0.65) # 设置图像透明度，无所谓
df.score[df.time >=2013].plot(kind='kde',color='steelblue')
df.score[df.time < 2013][df.time >= 2003].plot(kind='kde',color='lightblue')
df.score[df.time < 2003].plot(kind='kde',color='pink')
plt.xlabel(u"score")# plots an axis lable
plt.ylabel(u"probability")
plt.title(u"time & score")
plt.legend((u'latest(after 2013)', u'medium(2003-2013)',u'classic(before 2003)'),loc='best') # sets our legend for our graph.
plt.xlim(0,10)
plt.show()
plt.savefig('time & score.png')   # 保存图片

fig.set(alpha=0.65) # 设置图像透明度，无所谓
aa = df.score[df.time >=2013].value_counts()
bb = df.score[df.time < 2013][df.time >= 2003].value_counts()
cc = df.score[df.time < 2003].value_counts()
df2=pd.DataFrame({u'latest(after 2013)':aa, u'medium(2003-2013)':bb, u'classic(before 2003)':cc})
df2.plot(kind='bar', stacked=True)
plt.title(u"time & score")
plt.xlabel(u"score")
plt.ylabel(u"movie")
plt.show()
plt.savefig('time & score2.png')
#了解年份与分数的关系，一般来说越新越高分
df.boxplot(column='score', by='time')
plt.title(u"distribution of score")
plt.show()
plt.savefig('distribution of score2.png')   # 保存图片
#了解年份与分数的关系，一般来说越新分数的标准差越大，是异方差的（当然也与样本量有关）
#然而可见，1985-2005这一段时间，整体作品质量都比较上乘


fig.set(alpha=0.65) # 设置图像透明度，无所谓
df.score[df.people >= 70000].plot(kind='kde',color='steelblue')
df.score[df.people < 70000][df.people >= 7000].plot(kind='kde',color='lightblue')
df.score[df.people < 7000][df.people >=700].plot(kind='kde',color='pink')
df.score[df.people < 700].plot(kind='kde',color='red')
plt.legend((u'very famous(>70000 comments)', u'famous(7000-70000 comments)',u'medium(700-7000 comments)',u'low(<700 comments)'),loc='best') # sets our legend for our graph.
plt.xlim(0,10)
plt.xlabel(u"score")# plots an axis lable
plt.ylabel(u"probability")
plt.title(u"people & score")
plt.show()
plt.savefig('people & score.png')   # 保存图片

fig.set(alpha=0.65) # 设置图像透明度，无所谓
aa = df.score[df.people >= 70000].value_counts()
bb = df.score[df.people < 70000][df.people >= 7000].value_counts()
cc = df.score[df.people < 7000][df.people >=700].value_counts()
dd = df.score[df.people < 700].value_counts()
df2=pd.DataFrame({u'very famous(>70000 comments)':aa, u'famous(7000-70000 comments)':bb, u'medium(700-7000 comments)':cc, u'low(<700 comments)':dd})
df2.plot(kind='bar', stacked=True)
plt.title(u"people & score")
plt.xlabel(u"score")
plt.ylabel(u"movie")
plt.show()
plt.savefig('people & score2.png')   # 保存图片
#了解评价人数与分数的关系，一般来说评价人数与分数成正相关


fig.set(alpha=0.65) # 设置图像透明度，无所谓
df.time[df.people >= 70000].plot(kind='kde',color='steelblue')
df.time[df.people < 70000][df.people >= 7000].plot(kind='kde',color='lightblue')
df.time[df.people < 7000][df.people >=700].plot(kind='kde',color='pink')
df.time[df.people < 700].plot(kind='kde',color='red')
plt.legend((u'very famous(>70000 comments)', u'famous(7000-70000 comments)',u'medium(700-7000 comments)',u'low(<700 comments)'),loc='best') # sets our legend for our graph.
plt.xlim(1910,2030)
plt.xlabel(u"time")# plots an axis lable
plt.ylabel(u"probability")
plt.title(u"people & time")
plt.show()
plt.savefig('people & time.png')   # 保存图片

fig.set(alpha=0.65) # 设置图像透明度，无所谓
aa = df.time[df.people >= 70000].value_counts()
bb = df.time[df.people < 70000][df.people >= 7000].value_counts()
cc = df.time[df.people < 7000][df.people >=700].value_counts()
dd = df.time[df.people < 700].value_counts()
df2=pd.DataFrame({u'very famous(>70000 comments)':aa, u'famous(7000-70000 comments)':bb, u'medium(700-7000 comments)':cc, u'low(<700 comments)':dd})
df2.plot(kind='bar', stacked=True)
plt.title(u"people & time")
plt.xlabel(u"time")
plt.ylabel(u"movie")
plt.show()
plt.savefig('people & time2.png')   # 保存图片
#了解评价人数与年份的关系，一般来说评价人数与分数成正相关


df['score'] = pd.cut(df.score, bins=10, labels=False)
fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.scatter(df.time, df.score)
plt.ylabel(u"movie")                         # 设定纵坐标名称
plt.xlabel(u"year")# plots an axis lable
plt.grid(b=True, which='major', axis='y')
plt.title(u"time & score")
plt.show()
plt.savefig('time & score3.png')   # 保存图片
#老片分数一般很集中在6-9分的中高分段，新片则两极分化愈发严重。


fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.scatter(df.people, df.score)
plt.ylabel(u"movie")                         # 设定纵坐标名称
plt.xlabel(u"people")# plots an axis lable
plt.grid(b=True, which='major', axis='y')
plt.title(u"people & score")
plt.show()
plt.savefig('people & score3.png')   # 保存图片
#越高分的电影评分人数越多（越famous）


#下次解锁别的图？气泡图之类的？以及多维度的图。




