# Explorartry Data Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()

# print(iris.shape)
# print(iris.columns)

# print(iris["variety"].value_counts())

iris.plot(kind='scatter', x='sepal.length', y='sepal.width')

sns.set_style("whitegrid") # next line ma dot vadu function use karvu hoi tyare \ lagvi devanu
sns.FacetGrid(iris, hue='variety') \
    .map(plt.scatter,'sepal.length', 'sepal.width') \
    .add_legend()
plt.show()