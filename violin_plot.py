import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path=""
df = pd.read_excel(path)
df = df.iloc[:, 10:] # drop the first 10 columns
print(df.head()) # make sure everything is loaded right
plt.figure(figsize=(10, 6), dpi=500)
sns.violinplot(data=df)
ax = sns.violinplot(data=df, linewidth=0, inner="box")
ax.get_xaxis().set_visible(False)
plt.savefig("violin_plot.png", dpi=500)
plt.xticks(rotation=90)
plt.show()
