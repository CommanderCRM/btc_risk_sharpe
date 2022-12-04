import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = yf.Ticker("BTC-USD")

print(data.info['description'])

price = data.history('1y')['Close']

change = price.pct_change()
cum_returns = (change+1).cumprod()

cum_returns.plot()
plt.savefig("plot.png")


annual_std = np.std(cum_returns) * np.sqrt(252)
sharpe = (np.mean(cum_returns) / np.std(cum_returns))*np.sqrt(252)

print("Annual risk %:", annual_std*100)
print("Annual Sharpe ratio:", sharpe)
