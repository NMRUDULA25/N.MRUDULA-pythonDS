import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={'name':["a","b","c","d","e"],'age':[24,35,15,43,13],'dept':["IT","CSE","IOT","IT","CSE"],'salary':[15000,25000,34000,45000,16000],'joindate':pd.to_datetime(['2020-06-12','2021-03-07','2019-06-05','2018-08-23','2014-09-09'])}
df=pd.DataFrame(data)
# labels=df['name'].tolist()
# ages=df['age'].tolist()
# plt.bar(labels,ages,color="Green")
# plt.show()
# seaborn
# sns.barplot(x='name',y='age',data=df)
# plt.show()
# sns.barplot(x='dept',y='salary',data=df,estimator=sum)
# plt.show()
# sns.countplot(x='dept',data=df)
# plt.show()

#combine multiple charts in single frame
fig,axs=plt.subplots(1,3,figsize=(12,5))
sns.barplot(x='dept',y='salary',data=df,estimator=sum,ax=axs[0])
sns.countplot(x='dept',data=df,ax=axs[1])
sns.histplot(df['age'],kde=True,ax=axs[2])
plt.tight_layout()
plt.show()