<<<<<<< HEAD
#import libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


df=sns.load_dataset('titanic')
print(df)

df.head(10) # top 10
df.tail(10)  #bottom 10
df.sample(10)

missing= df.isnull().sum()
print(missing)
col= df.columns
print(col)

drop_deck=df.drop(['deck'],axis=1,inplace=True)
print(drop_deck)

df['age']=df['age'].fillna(df['age'].mean())

print(df['age'])
print(df['age'].mean())

df['embarked'].nunique()
town=df['embarked'].value_counts()
print(town)

df['embarked'] = df['embarked'].fillna('S')
df['embarked']

new_name=df.rename(columns={'sex':'gender'},inplace=True)
print(new_name)

plt.figure(figsize=(5,7))
sns.countplot(x='pclass',hue='alive',data=df)
plt.show()

plt.figure(figsize=(5,7))
sns.countplot(x='embark_town',hue='alone',data=df)
plt.show()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
#df['encoded_gender']=le.fit_transform(df['gender'])
df.head()

num_df=df.select_dtypes(include=['number'])
corr=num_df.corr()
print(corr)

sns.heatmap(corr,cmap='rocket')
=======
#import libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


df=sns.load_dataset('titanic')
print(df)

df.head(10) # top 10
df.tail(10)  #bottom 10
df.sample(10)

missing= df.isnull().sum()
print(missing)
col= df.columns
print(col)

drop_deck=df.drop(['deck'],axis=1,inplace=True)
print(drop_deck)

df['age']=df['age'].fillna(df['age'].mean())

print(df['age'])
print(df['age'].mean())

df['embarked'].nunique()
town=df['embarked'].value_counts()
print(town)

new_town=df['embarked'].fillna('S',inplace=True)
new_town=df['embarked'].isnull().sum()
print(new_town)

new_name=df.rename(columns={'sex':'gender'},inplace=True)
print(new_name)

plt.figure(figsize=(5,7))
sns.countplot(x='pclass',hue='alive',data=df)
plt.show()

plt.figure(figsize=(5,7))
sns.countplot(x='embark_town',hue='alone',data=df)
plt.show()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
#df['encoded_gender']=le.fit_transform(df['gender'])
df.head()

num_df=df.select_dtypes(include=['number'])
corr=num_df.corr()
print(corr)

sns.heatmap(corr,cmap='rocket')
>>>>>>> cd45f04a90226f3a16fb96525526f55ee41853bd
