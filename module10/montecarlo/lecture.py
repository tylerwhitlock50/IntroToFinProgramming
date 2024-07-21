import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

"""
slots = 10
tries = 1000

outcomes = np.random.randint(0, slots, tries)
outcomes = pd.Series(outcomes).rename('outcomes')
expected = pd.Series(np.full(slots, tries/slots)).rename('expected')
plt.hist(outcomes,bins=slots, color='blue')
plt.plot(expected, color='red')
plt.show()
"""
""" 
Random walk
"""

# Random walk simulation
stock = yf.Ticker('AAPL')
history = stock.history(period='1y')
change = history['Close'].pct_change().dropna()
change = change + 1
mean = change.mean()
std_dev = change.std()
print(f"Mean: {mean}, std_dev: {std_dev}")

last_price = history['Close'].iloc[-1]
simulated_paths = []

for _ in range(100):  # 100 simulated paths
    prices = [last_price]
    for _ in range(252):  # 252 trading days
        new_price = prices[-1] * np.random.normal(mean, std_dev)
        prices.append(new_price)
    simulated_paths.append(prices)

simulated_df = pd.DataFrame(simulated_paths).T #create a dataframe
average_path = simulated_df.mean(axis=1)
percentile_95 = simulated_df.quantile(0.95, axis=1)

# Plotting the simulated paths
for path in simulated_paths:
    plt.plot(path, alpha=0.3, color='blue')

# Plotting the average path
plt.plot(average_path, color='red', linewidth=2, label='Average Path')
plt.plot(percentile_95, color='green', linewidth=2, label='95th Percentile')

plt.title("Simulated Random Walk Paths for AAPL")
plt.xlabel("Trading Days")
plt.ylabel("Price")
plt.legend()
plt.show()