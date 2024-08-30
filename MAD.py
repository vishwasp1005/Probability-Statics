# Meadian Absolute Deviation

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels import robust 
# to use mad

iris = pd.read_csv('iris.csv')
iris.head()
iris_setosa = iris.loc[iris['variety'] == "Setosa"]
iris_virginica = iris.loc[iris['variety'] == "Virginica"]
iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]

print("MAD = ")
print(robust.mad(iris_setosa['petal.length']))
print(robust.mad(iris_virginica['petal.length']))
print(robust.mad(iris_versicolor['petal.length']))