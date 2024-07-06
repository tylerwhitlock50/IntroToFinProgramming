import pandas_datareader as wb
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Set start and end dates
start = datetime(2017, 1, 1)
end = datetime.today()

# Download data
usd = wb.DataReader('IRSTCI01USM156N', 'fred', start, end)
eur = wb.DataReader('IRSTCI01EZM156N', 'fred', start, end)  # Corrected code
fx = wb.DataReader('DEXUSEU', 'fred', start, end)

# Drop NaN
usd.dropna(inplace=True)
eur.dropna(inplace=True)
fx.dropna(inplace=True)

# Merge data
data = pd.concat([usd, eur, fx], axis=1)
data.columns = ['USD', 'EUR', 'FX']

# Calculate difference
data['diff'] = abs(data['USD'] - data['EUR'])

# Calculate percent change
data['FX_pct'] = data['FX'].pct_change()
data['diff_pct'] = data['diff'].pct_change()

# Drop NaN
data.dropna(inplace=True)

# Regress
X = data['diff_pct'].values.reshape(-1, 1)
y = data['FX_pct'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Calculate r2 score
r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2}")

data.to_excel('data.xlsx')

# Plot
plt.scatter(data['diff_pct'], data['FX_pct'], color='blue', label='Data points')
plt.plot(X_test, y_pred, color='red', label='Regression line')
plt.xlabel('Difference in rates')
plt.ylabel('FX rate')
plt.title('Difference in rates vs FX rate')
plt.legend()
plt.show()
