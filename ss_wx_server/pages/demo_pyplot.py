import streamsync as ss

import seaborn as sns
import matplotlib as mpl
mpl.use("Agg") #很重要，否则在ss中会崩溃
import matplotlib.pyplot as plt


#下载不了，所以加一个参数data_home
data_home = "./data/seaborn"

ss.heading("演示matplotplotg功能")

ss.text("1. 画折线图")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic", data_home=data_home)
sns.lineplot(x="age", y="fare", hue="sex", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.text("2. 画散点图")

sns.set_style("whitegrid")
tips = sns.load_dataset("tips", data_home=data_home)
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")

ss.text("3. 画条形图")

sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.barplot(x="class", y="survived", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")


ss.text("4. 画直方图")
sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic",data_home=data_home)
sns.histplot(x="age", data=titanic)
plt.show()

fig = plt.gcf()
ss.pyplot(fig, style="border:1px solid gray; width:600px")
