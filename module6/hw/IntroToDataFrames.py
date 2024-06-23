import pandas_datareader.data as wb
import datetime as date
import pandas as pd
#Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
#(https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016:
#6-Month
#1-Year
#5-Year
#10-Year
#Step 2( 5 points ): Determine the average and standard deviation for each of the maturities( maturity is 6-month, 1 year, etc.)
#Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
#Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities
#has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
#Step 5( 5 points): Save the generated dataframe as sigma.xlsx
#Please upload this filled file and sigma.xlsx


# Define the varibles needed for the assignment
maturities = ['DTB6', 'DTB1YR', 'DGS5', 'DGS10'] #daily data set
#maturities = ['GS6M', 'GS1', 'GS5', 'GS10'] #monthly Maturities
columns = ['6-Month', '1-Year', '5-Year', '10-Year']
start, end =  date.datetime(2014, 2, 1), date.datetime(2016, 2, 1)

#Step 1 (Build DataFrame)
df = pd.concat([wb.DataReader(m,'fred',start,end) for m in maturities],axis=1) 
df.columns = columns

#Step 2 (Calculate Stats)
stats = df.describe().loc[['mean','std']] 

# Step 3 (Filter) / Step 4 (Drop NAN)
filtered_df = (df[(df < (stats.loc['mean'] - stats.loc['std'])) 
                 | (df > (stats.loc['mean'] + stats.loc['std']))]
                .dropna() 
                    )

# Step 5 (Svae to Excel)
filtered_df.to_excel('sigma.xlsx')
print(filtered_df)


