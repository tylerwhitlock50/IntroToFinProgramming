import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('oilprices.csv')


#price.plot().set(ylabel='Price', title='Oil Prices')
#plt.show()
#data.plot().set(ylabel='Price', title='Oil Prices')
#plt.show()
price = data['Price'].values
price_30 = data['Price'].rolling(window=30).mean().values
index = data.index.values

def create_line_plot(x,y):
    plt.plot(x, y, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=2)
    plt.title('Oil Prices')
    plt.xlabel('Price')
    plt.ylabel('Index')
    plt.show()

def create_plot_with_rolling(x,y,rolling):
    plt.plot(x, y, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=2)
    plt.plot(x, rolling, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=2)
    plt.title('Oil Prices')
    plt.xlabel('Price')
    plt.ylabel('Index')
    plt.show()

create_line_plot(index,price)
create_plot_with_rolling(index,price,price_30)