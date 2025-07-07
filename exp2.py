import pandas as pd
data={'name':["a","b","c","d","e"],'age':[24,35,15,43,13],'dept':["IT","CSE","IOT","IT","CSE"],'salary':[15000,25000,34000,45000,16000],'joindate':pd.to_datetime(['2020-06-12','2021-03-07','2019-06-05','2018-08-23','2014-09-09'])}
print(data)
df=pd.DataFrame(data)
print(df)
print(df.head(3)) #it will print first 3 records
print(df.shape) #it will print size of dataframe(5,5)
print(df.dtypes) #it will print datatypes of each column
arr=df.columns.tolist()
print(arr)
#Filtering
#column Based Filtering
print(df[['name','dept']])
#Based on column and value
print(df[df['dept']=="IT"])
print(df[df['salary']>20000])
print(df[(df['dept']=="CSE") & (df['salary']>2000)]) #Based on department and salary multiple columns
print(df['salary'].max()) #Find who getting more salary
print(df.groupby('dept')['salary'].sum()) #Groupby dept and sum of each department
print(df['dept'].value_counts()) #it will prints count of each dept
df['bonus']=df['salary']*0.10 #adding new column with calculation 
print(df)
df['joiningyear']=df['joindate'].dt.year #to collect the joining year
df['joiningmonth']=df['joindate'].dt.month #to collect the joining month
print(df)
df.rename(columns={'joindate':'joiningdate'},inplace=True) ##Renaming the column
print(df)
df.drop(columns=['joiningmonth'],inplace=True) ##Droping a column
print(df)
df=df.sort_values(by='salary',ascending=True) ##sorting
print(df)
print(df.loc[df.groupby('dept')['salary'].idxmax()]) #fetch who  is getting more salary in each department
df['seniority']=df['age'].apply(lambda x:'senior' if x>30 else 'junior') #seniority based on age
print(df)
df.to_csv("employee.csv",index=False)