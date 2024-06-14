import pandas_datareader as pdr


# Load data from fred for us gdp
df = pdr.DataReader('GDP', 'fred')
print(df.index)
print(df.columns)
print(df.head())
print(df.dtypes())
print(df.describe())