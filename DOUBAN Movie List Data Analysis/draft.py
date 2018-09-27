import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import codecs
pd.options.mode.chained_assignment = None

df = pd.read_csv("score.csv") #读取数据
print(df.shape)
print(df.info())
print(df.describe())


df.ix[df.time.isnull(),'time'] = 2010#处理缺失值，按平均值填充
df.ix[df.people.isnull(),'people'] = 3569#处理缺失值，按平均值填充
df.ix[df.score.isnull(),'score'] = 7.3#处理缺失值，按平均值填充

from sklearn.preprocessing import StandardScaler
df['people'] = StandardScaler().fit_transform(df.people.values.reshape(-1,1))


def cap_values(x, cap):
    if x > cap:
        return cap
    else:
        return x
# 设定上限
df.people = df.people.apply(lambda x: cap_values(x, 100000))
fig=plt.figure()
fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.scatter(df.people,df.score)
plt.ylabel(u"score")
plt.xlabel(u"people")# plots an axis lable
plt.grid(b=True, which='major', axis='y')


df_up = df.as_matrix()
print(df_up.shape)
print(df.info())
print(len(df_up[1]))
print(len(df_up[2]))
print(df_up[1].shape)
print(df_up[2].shape)
x = df_up[2]
y = df_up[1]


# Function to know which Tv show will have more viewers
regr = linear_model.LinearRegression
regr.fit(x[:, np.newaxis],y)
pred_y = regr.predict(x[:, np.newaxis])
print(pred_y)
plt.plot(x, pred_y, linewidth=2)
plt.xlabel("people")
plt.ylabel("score")
plt.title("people-score regression")
plt.grid()
plt.show()


