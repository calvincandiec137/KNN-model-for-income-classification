# To work with dataframes
import pandas as pd 

# To perform numerical operations
import numpy as np

# To visualize data
import seaborn as sns

# To partition the data
from sklearn.model_selection import train_test_split

# importing the library of KNN
from sklearn.neighbors import KNeighborsClassifier  

# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix


###############################################################################

########################importing data#########################################

data_income=pd.read_csv('income.csv',na_values=[" ?"])
data=data_income.copy()

#############################Data Pre processing###############################

null_data=data.isnull().sum()
print(null_data)

missing = data[data.isnull().any(axis=1)]

data2=data.dropna(axis=0)

# Reindexing the salary status names to 0,1
data2['SalStat']=data2['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
print(data2['SalStat'])

new_data=pd.get_dummies(data2,drop_first=True)


# Storing the column names 
column_list=list(new_data.columns)
print(column_list)


# Separating the input names from data
features=list(set(column_list)-set(new_data['SalStat']))
print(features)

y=new_data['SalStat'].values
print(y)

x = new_data[features].values
print(x)

train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)

# Storing the K nearest neighbors classifier
KNN_classifier = KNeighborsClassifier(n_neighbors = 5)  

# Fitting the values for X and Y
KNN_classifier.fit(train_x, train_y) 

# Predicting the test values with model
prediction = KNN_classifier.predict(test_x)

# Performance metric check
confusionMmatrix = confusion_matrix(test_y, prediction)
print(confusionMmatrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)

print('Misclassified samples: %d' % (test_y != prediction).sum())

"""
Effect of K value on classifier
"""
Misclassified_sample = []
# Calculating error for K values between 1 and 20
for i in range(1, 20):  
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_x, train_y)
    pred_i = knn.predict(test_x)
    Misclassified_sample.append((test_y != pred_i).sum())

print(Misclassified_sample)