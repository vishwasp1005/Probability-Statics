import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv')

sns.violinplot(x='variety', y = 'petal.length', data=iris)
plt.grid(True)
plt.show()