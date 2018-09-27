import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

x = np.arange(0, 1, 0.002)
y = norm.rvs(0, size=500, scale=0.1)
y = y + x ** 2


plt.scatter(x, y, s=5)
degree = [1, 2, 100]
y_test = []
y_test = np.array(y_test)

for d in degree:
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', LinearRegression(fit_intercept=False))])
    clf.fit(x[:, np.newaxis], y)
    y_test = clf.predict(x[:, np.newaxis])

    print(clf.named_steps['linear'].coef_)
    print( clf.score(x[:, np.newaxis], y))

    plt.plot(x, y_test, linewidth=2)

plt.grid()
plt.legend(['1', '2', '100'], loc='upper left')
plt.show()

print(x[:, np.newaxis].shape)
print(y.shape)

