# Sample Exemple Of Regression Liniare Parfait
from sklearn.datasets import make_regression

from matplotlib import pyplot

X_test, y_test = make_regression(n_samples=150, n_features=1, noise=0.2)

pyplot.scatter(X_test,y_test)
pyplot.show()
