import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")
sns.boxplot(x='variety', y='petal.length', data=iris, palette=["skyblue", "lightgreen", "salmon"])
plt.show()