import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
pd.options.mode.chained_assignment = None
import codecs
df1 = pd.ExcelFile("三因素分析表-2017.06-0705-1.xlsx") #读取数据
df = df1.parse('三因素分析')
print(df.shape)
print(df.info())
print(df.describe())