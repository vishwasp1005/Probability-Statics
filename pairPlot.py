import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")
iris.head()

#4c2 graphs aavse
sns.set_style('whitegrid')
sns.pairplot(iris, hue='variety', height=3)
plt.show()