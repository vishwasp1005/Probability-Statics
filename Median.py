import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()
iris_setosa = iris.loc[iris['variety'] == "Setosa"]
iris_virginica = iris.loc[iris['variety'] == "Virginica"]
iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]

print("Median = ")
print(np.median(iris_setosa['petal.length']))
print(np.median(np.append(iris_setosa['petal.length'],50)))
print(np.median(iris_virginica['petal.length']))
print(np.median(iris_versicolor['petal.length']))

# Output of Mean:
# Means = 
# 1.4620000000000002
# 2.4137254901960787
# 5.5520000000000005
# 4.26

print("\nQuantile")
print(np.percentile(iris_setosa['petal.length'],np.arange(0,100,25)))
print(np.percentile(iris_virginica['petal.length'],np.arange(0,100,25)))
print(np.percentile(iris_versicolor['petal.length'],np.arange(0,100,25)))

print("\nPercentile")
print(np.percentile(iris_setosa['petal.length'],90))
print(np.percentile(iris_virginica['petal.length'],90))
print(np.percentile(iris_versicolor['petal.length'],90))