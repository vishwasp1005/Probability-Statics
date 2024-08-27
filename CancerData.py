import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('haberman.csv')
df.columns = ["age", "operation_year", "aln", "survival_status"]
# here aln = axillary_lymph_node (Doctor ni bhasha)

df['survival_status'] = df['survival_status'].map({1:'yes', 2:'no'})
# to replace data

print(df['survival_status'].value_counts())
# yed and no count

status_yes = df[df['survival_status'] == 'yes']
print(status_yes.describe())
status_no = df[df['survival_status'] == 'no']
print(status_no.describe())
# to print data of yes/no

df.head()
# print(df.describe())
# print(df)

sns.FacetGrid(df,hue='survival_status', height=5).map(sns.distplot, 'aln').add_legend()
plt.grid(True)
plt.show()

# find CDF

count1, edge1 = np.histogram(status_yes['aln'], bins=10, density=True)
pdf1 = count1 / (sum(count1))
print(pdf1)
print(edge1)
cdf1 = np.cumsum(pdf1)
plt.plot(edge1[1:], pdf1)
plt.plot(edge1[1:], cdf1, label = 'yes')
plt.xlabel('nodes')

print("-------------------------------------------------------------------")

count2, edge2 = np.histogram(status_no['aln'], bins=10, density=True)
pdf2 = count2 / (sum(count2))
print(pdf2)
print(edge2)
cdf2 = np.cumsum(pdf2)
plt.plot(edge2[1:], pdf2)
plt.plot(edge2[1:], cdf2, label = 'no')
plt.xlabel('nodes')
plt.legend()
plt.show()

# box plot

# sns.boxplot(x='survival_status', y='age', data=df)
# plt.show()
# sns.boxplot(x='survival_status', y='operation_year', data=df)
# plt.show()
# sns.boxplot(x='survival_status', y='aln', data=df)
# plt.show()


# pair plot

# sns.set_style('whitegrid')
# sns.pairplot(df,hue='survival_status', height=5)
# plt.show()


#multivariate analysis 

sns.jointplot(x='operation_year', y='age', data=df, kind='kde', cmap='viridis', fill=True)
plt.show()