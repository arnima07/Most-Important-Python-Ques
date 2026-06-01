# categorial to numerical conversion in python

import pandas as pd
import sklearn



data= {
       'name': ['A', 'B', 'C', 'D'],
       'Gender': ['male', 'female', 'female','male'],
       'city': ['delhi', 'noida', 'delhi','mumbai'],
       'purchased': ['yes', 'no', 'yes','no']
       }
df=pd.DataFrame(data)
print(df)

#1 identify categorical columns in a given dataset

idt=df.select_dtypes(include='object').columns
print(idt)

inf=df.info
print(inf)

#2 apply label encoding on a "gender" column

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Encoded_gender'] = pd.Series(le.fit_transform(df['Gender']), index=df.index)
lec = df['Encoded_gender']
print(lec)


#3 convert a 'city' column using one-hot encoding

dummies=pd.get_dummies(df['city'], drop_first=True)
df=pd.concat([df,dummies],axis=1)
print(df)
print(dummies)

#4 list all unique categories ina a column using pandas

df.columns
num =df['city'].value_counts()
print(num)

#7 convert a binary column (yes/no) into(0/1) manually

df['encoded_purchase']=df['purchased'].map({'yes':0,'no':1})
print(df)


 