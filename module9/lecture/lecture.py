import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, classification_report
from sklearn.preprocessing import StandardScaler

from WOE_updated_modern import data_vars

# Load the data
df = pd.read_csv('150k.csv')
print(df.head())
print(df.info())
print(df.describe())  

nums = df.select_dtypes(include=[np.number]).fillna(100) 
category = pd.get_dummies(df.select_dtypes(include=[object]))
corr = nums.corr()
#sns.heatmap(corr, annot=True, fmt=".2f")
#plt.show()

corr.to_excel('correlation.xlsx')

corr_matrix = nums.corr().abs()
# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.7)]
df_reduced = nums.drop(columns=to_drop)

#sns.heatmap(df_reduced.corr(), annot=True, fmt=".2f")
#plt.show()

y = df_reduced['default_ind']
x = df_reduced.drop(columns=['default_ind'])

result = data_vars(x, y)
print(result)
#result[0].to_excel('woe.xlsx')
#result[1].to_excel('iv.xlsx')

vars = result[0].loc[(result[0]['IV'] > 0.02) & (result[0]['IV'] < 1.00) , 'VAR_NAME'].unique()
print(vars)


# join the category and numerical data
x = x[vars].join(category)
x = StandardScaler().fit_transform(x) #scale the data
#print(x.head()) # this is no longer a dataframe
y = y #no change

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=1) #create the training and testing sets

model = LogisticRegression(max_iter=5000) #create the model
model.fit(xtrain, ytrain) #fit the model

print(model.score(xtest, ytest)) #print the accuracy of the model
print(roc_auc_score(ytest, model.predict(xtest))) #print the AUC score
print(classification_report(ytest, model.predict(xtest))) #print the classification report
print(confusion_matrix(ytest, model.predict(xtest))) #print the confusion matrix

#model.coef_ #print the coefficients
#model.intercept_ #print the intercept

#ypred = model.predict(xtest) #predict the test set
#print(confusion_matrix(ytest, ypred)) #print the confusion matrix

