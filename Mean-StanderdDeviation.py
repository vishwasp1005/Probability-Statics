import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = pd.read_csv('iris.csv')
iris.head()
iris_setosa = iris.loc[iris['variety'] == "Setosa"]
iris_virginica = iris.loc[iris['variety'] == "Virginica"]
iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]

# use "mean" for Mean and use "std" for standers deviation in NumPy
print("Means = ")
print(np.mean(iris_setosa['petal.length']))
print(np.mean(np.append(iris_setosa['petal.length'],50)))
print(np.mean(iris_virginica['petal.length']))
print(np.mean(iris_versicolor['petal.length']))

print("Std-Dev = ")
print(np.std(iris_setosa['petal.length']))
print(np.std(iris_virginica['petal.length']))
print(np.std(iris_versicolor['petal.length']))
