import pandas as pd
import numpy as np

from WOE_updated_modern import data_vars
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics

def printOutTheCoefficients(params, coeffecients, intercept):
    tParams = np.array(params)[:, np.newaxis]  # Convert to NumPy array and add new axis
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams, tCoeffs], axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)
    
#load the data from the dataset
df = pd.read_csv('adultIncome_proc.csv')
df.columns = df.columns.str.lower().str.strip().str.replace(' ','_').str.replace('-','_')
print(df.columns)
#drop obviously correlated values
num_df = df[['age','hours_worked','years_of_education']].astype(float)
cat_df = df[['type_of_employment','occupation','degree','martial_status','race','sex','native_country']]
y_df = df['income_80k+'].astype(float)

print(num_df.describe())
print(cat_df.describe())
print(y_df.describe())

#reduce Marial Status to four  categories -- Married, Separated, Never Married, Widowed
def get_first_word(x:str):
    return x.split('-')[0]

#map countries to born in United States or not
def is_US(x:str):
    return 1 if x == 'United-States' else 0

cat_df['marial_status'] = df['martial_status'].apply(get_first_word)
cat_df['native_country'] = df['native_country'].apply(is_US)

#determine if any fields are correlated with each other
corr = pd.concat([num_df,y_df],axis=1).corr()
#find statistically significant or unreasonable variables using WOE file
x = data_vars(df,y_df)
print(x)
#dummy encode all of the non-quantitative values

dummies = pd.get_dummies(cat_df)
#drop dummyfied variables

#create table with base quantitative values and with dummy values
final = pd.concat([num_df,dummies],axis=1)
#separate for resutls and input sets

#split between sets
xtrain, xtest, ytrain, ytest = train_test_split(final,y_df,test_size=0.2,random_state=1)
#run logistic regresstion
model = LogisticRegression()
model.fit(xtrain,ytrain)
#print classification report

print(classification_report(ytest,model.predict(xtest)))

#print resuls using printOutCoefficients method to excel and run 5 different rows through the model in excel
printOutTheCoefficients(final.columns,model.coef_,model.intercept_)
