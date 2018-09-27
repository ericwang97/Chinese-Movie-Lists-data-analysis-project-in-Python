import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn import linear_model
pd.options.mode.chained_assignment = None
import codecs
df = pd.read_csv("score.csv") #读取数据
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)


df.ix[df.time.isnull(),'time'] = 2010#处理缺失值，按平均值填充
df.ix[df.people.isnull(),'people'] = 3569#处理缺失值，按平均值填充

score = KNeighborsRegressor(n_neighbors=1)#使用K-means方法填充分数 #n_neighbors即KNN中的K值

# 把数据分为两部分，有缺失的和无缺失的，用无缺失的数据建立模型来判断缺失数据的可能取值
train_score = df[df.score.isnull()==False] #训练集
train_null_score = df[df.score.isnull()==True]
cols = ['time', 'people']
score.fit(train_score[cols], train_score.score)
new_values = score.predict(train_null_score[cols])
train_null_score.ix[:, 'score'] = new_values #填充分数缺失值
score = train_score.append(train_null_score)
df.score = score
print(df.info())
print(score)

#填充的score为5.6分？？？？（这是为何）（统计学知识用到了）
#难道要一个个迭代？？？
#处理缺失值
