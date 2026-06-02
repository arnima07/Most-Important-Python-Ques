# NumPy is a powerful library in Python for numerical computing.
# It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
# Here are some key features and functionalities of NumPy:




import numpy as np


arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
result=arr1+arr2
print(result)

arr3=np.array([[1,0,0],[0,1,0],[0,0,1]])
print(arr3)

arr4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4)

print(arr4.T)


matrix=np.eye(3)
print(matrix)

arr7=np.arange(20)
print(arr7)

arr=np.array([12,15,18,20,22,25])
print(arr)

mean_is=np.mean(arr)
print(mean_is)
median_is=np.median(arr)
print(median_is)

matA=np.array([[2,1],[1,3]])
matB=np.array([[8],[13]])
results=np.linalg.solve(matA,matB)
print(results)
matC=np.array([[2,1],[1,1]])
matD=np.array([[8],[5]])
results2=np.linalg.solve(matC,matD)


#how to find the inverse of a matrix
matE=np.array([[2,1],[1,3]])
inverse=np.linalg.inv(matE)
print(inverse)

#how to find the determinant of a matrix
matF=np.array([[2,1],[1,3]])
determinant=np.linalg.det(matF)
print(determinant)



# how to handle missing values in numpy

import pandas as pd
import numpy as np

data={'name':['Arpit','Aman','Neha','Riya','Preeti','Raman','Naman'],
       'age': [18, 19, 20, np.nan, 22, 17, 18],
       'marks': [90, 70, np.nan, 76,80,95,40],
       'City' :['RKE','DDN','LKO','MUM',np.nan,np.nan,np.nan]
       }
df=pd.DataFrame(data)
print(df)

df.isnull().sum()
df.info()
miss_per=(df.isnull().sum()/len(df))*100
print(miss_per)
       
#remove rows that contain missing values
rem_row=df_rem_rows=df.dropna()
print(rem_row)

#remove columns that contains missing values
rem_mis=df_rem_col=df.dropna(axis=1)
print(rem_mis)

#fill missing numerical values using mean of the column
df_mean=df
df_mean['age'].fillna(df_mean['age'].mean(),inplace=True)
df_mean['marks'].fillna(df_mean['marks'].mean(),inplace=True)
df_mean['City'].fillna('unknown',inplace=True)

#fill missi values using a const value
df_const=df
replace=df_const.fillna({'age':0,'marks':0,'City':'unknown'},inplace=True)
print(replace)

#replace missing values using forward fill method.
df_ward=df.copy()
fill=df_ward.ffill()
print(fill)
#replace missing values using backward fill method.
df_back=df.copy()
# fill the values with median
#create a visualisation heatmap 
import seaborn as sns
map=sns.heatmap(df.isnull(),cmap="viridis")
print(map)



