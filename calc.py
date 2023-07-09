#imports
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as panda

#pulling and parsing data from AlphaVantage API
symbol = input('Enter symbol of desired stock: ')
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=0IUTAP2M1MBDCBOX'
r = requests.get(url)
data = r.json()
time_series = data["Time Series (5min)"]

#defining arrays in numpy
opens = np.array([float(entry["1. open"]) for entry in time_series.values()])
timestamps = np.array(list(time_series.keys()), dtype=np.datetime64)

#pandas dataframe (makes data savable to CSV)
dataframe = panda.DataFrame(timestamps, opens)
dataframe.to_csv('data.csv', sep='\t')

#matplotlib visualization
plt.plot(opens, timestamps)
plt.xlabel("Time")
plt.ylabel("Opens")
plt.title(f"Open Time Series: {symbol}")
plt.show()

