import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('haberman.csv')
df.columns = ["age", "operation_year", "aln", "survival_status"]

nodes = df['aln']
sm.qqplot(nodes, line='s')
plt.title('Q-Q Plot of Number of Positive Axillary Nodes')
plt.show()