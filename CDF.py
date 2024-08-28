#  Cumulative Distribution Function

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()
iris_setosa = iris.loc[iris['variety'] == "Setosa"]
iris_virginica = iris.loc[iris['variety'] == "Virginica"]
iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]

# bins -> means how many data u want in graph
count1, edges1 = np.histogram(iris_setosa['petal.length'], bins=10, density=True)
pdf1 = count1 / sum(count1)
cdf1 = np.cumsum(pdf1)

count2, edges2 = np.histogram(iris_virginica['petal.length'], bins=10, density=True)
pdf2 = count2 / sum(count2)
cdf2 = np.cumsum(pdf2)

count3, edges3 = np.histogram(iris_versicolor['petal.length'], bins=10, density=True)
pdf3 = count3 / sum(count3)
cdf3 = np.cumsum(pdf3)

# for PDF
plt.plot(edges1[1:], pdf1, label="Setosa PDF")
plt.plot(edges2[1:], pdf2, label="Virginica PDF")
plt.plot(edges3[1:], pdf3, label="Versicolor PDF")

#for CDF
plt.plot(edges1[1:], cdf1, label="Setosa CDF", linestyle='--')
plt.plot(edges2[1:], cdf2, label="Virginica CDF", linestyle='--')
plt.plot(edges3[1:], cdf3, label="Versicolor CDF", linestyle='--')
plt.xlabel('Petal Length')
plt.ylabel('Probability')
plt.grid(True)
plt.show()