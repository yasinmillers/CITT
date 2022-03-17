
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import mplfinance as mpf


plt.style.use('dark_background')

start = dt.datetime(2021, 3, 17)
end = dt.datetime.now()


def riot():
    stock = yf.download("RIOT", start="2022-01-17", end="2022-02-17")

    return stock


print(riot())


mpf.plot(stock_data, type='candlestick',
         volume=True, style='yahoo', title='APPL')
mpf.show
