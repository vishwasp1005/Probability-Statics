import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()

# iris_setosa = iris.loc[iris['variety'] == "Setosa"]
# iris_virginica = iris.loc[iris['variety'] == "Virginica"]
# iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]
# plt.plot(iris_setosa["petal.length"], np.zeros_like(iris_setosa["petal.length"]),'o')
# plt.plot(iris_virginica["petal.length"], np.zeros_like(iris_virginica["petal.length"]),'o')
# plt.plot(iris_versicolor["petal.length"], np.zeros_like(iris_versicolor["petal.length"]),'o')


sns.FacetGrid(iris, hue='variety', height=5)\
    .map(sns.distplot, 'petal.length')\
    .add_legend()


plt.show()