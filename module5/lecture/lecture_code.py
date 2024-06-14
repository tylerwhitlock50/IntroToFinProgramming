import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime as dt
import datetime

csv_file = r'external_data\ruger_stock.csv'
if not os.path.exists(csv_file):
    import yfinance as yf #swapped for pd_datareader as pandas-datareader is not working on my enviorment
    # Load data from yfinance and save it as a csv file
    ticker = 'RGR'
    today = dt.today().strftime('%Y-%m-%d')
    last_year = (dt.today() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
    df = yf.download(ticker, start=last_year, end=today)
    df.to_csv('external_data/ruger_stock.csv')

# Load the data from the csv file
df = pd.read_csv('external_data/ruger_stock.csv', index_col='Date', parse_dates=True)

print(df.index)
print(df.columns)
print(df.head(5))
print(df.tail(10))

#call out a row
row = df.loc['2024-01-02']
print(row)


#call out a column
column = df[['Close']] # as a dataframe
series = df['Close'] # as a series
print(type(column))   
print(type(series))

cols = ['Open','High']
plot = False # set to True to plot the data
if plot:
    df[cols].plot()
    plt.show()

#describe the data
print(df.describe())

df['dollar_volume'] = df['Close'] * df['Volume']
print(df.head(5))

#calculate the moving average
df['MA'] = df['Close'].rolling(window=10).mean()
print(df.head(15))

#calculate the std deviation
df['std'] = df['Close'].rolling(window=10).std()
print(df.head(15))
plot = False
if plot:
    df[['Close','MA','std']].plot()
    plt.title('Ruger Stock Price')
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.show()


df['returns'] = df['Close'] - df['Close'][0]
print(df.head(5))   

df['daily_change'] = df['Close'].diff()
df['pct_daily_change'] = df['Close'].pct_change()
print(df.head(5))

drop_cols = ['dollar_volume','MA','std','returns','daily_change','pct_daily_change']
df.drop(columns=drop_cols, inplace=True)

print(df.head(5))

df['percent_change'] = df['Close'].pct_change()
percent = .01
dfOnePercent = df[(df['percent_change'] > percent)| (df['percent_change'] < -percent)]
print(dfOnePercent.index)

dfOnePercent = dfOnePercent.sort_values(by='percent_change', ascending=False)
print(dfOnePercent.index)


#join the data This join doesn't make sese, becuase i'm adding back in the same data
joined_data = df.join(dfOnePercent, how='inner', lsuffix='_left', rsuffix='_right')

merged_data = df.merge(dfOnePercent, how='inner', left_index=True, right_index=True) # This is the prefferred way of joining data as it has more options
print(merged_data.index)

