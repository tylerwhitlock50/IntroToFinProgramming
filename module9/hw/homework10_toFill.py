import pandas as pd
import numpy as np

from HW8.WOE import data_vars
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics

def printOutTheCoefficients(params,coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,tCoeffs],axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)

#load the data from the dataset

#drop obviously correlated values

#reduce Marial Status to four  categories -- Married, Separated, Never Married, Widowed

#map countries to born in United States or not

#determine if any fields are correlated with each other

#find statistically significant or unreasonable variables using WOE file

#dummy encode all of the non-quantitative values

#drop dummyfied variables

#create table with base quantitative values and with dummy values

#separate for resutls and input sets

#split between sets

#run logistic regresstion

#print classification report

#print resuls using printOutCoefficients method to excel and run 5 different rows through the model in excel
