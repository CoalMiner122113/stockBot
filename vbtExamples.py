import numpy as np
import pandas as pd
from datetime import datetime as dt
import vectorbt as vbt
import yfinance as yf
import pandas_ta as ta

##I'm using this as playground to test out vectorbt, pandas_ta, and yfinance

start = '2019-01-01'
end = '2021-01-01'

#Using just YFinance
#Gets Open, High, Low, Close, Adj Close, and Volume
btcYFPrice1 = yf.download('BTC-USD', start=start, end=end)
#Gets a ticker object
btcYFPrice2 = yf.Ticker('BTC-USD')
#the ticker object can then be used to get historical data, which is identical to the yf.download() function
#but with added dividends and stock splits
btcYFPrice2.history(start=start, end=end)

#Using just VBT
#Gets Open, High, Low, Close, Volume, Dividends, Stock Splits
btcVBTPrice1 = vbt.YFData.download('BTC-USD', start=start, end=end)
#Gets Date and close price
btcVBTPrice1.get('Close')

#Using just Pandas-TA
#Gets Open, High, Low, Close, Volume, Dividends, Stock Splits
#From 2014-9-17 to 2023-6-27 (Today's date)
bctTAPrice1 = pd.DataFrame().ta.ticker('BTC-USD')

#Can we convert them all to pandas dataframes?
#Yes, and their shape is as mentioned above
df1 = pd.DataFrame(btcYFPrice1)
df2 = pd.DataFrame(btcYFPrice2.history(start=start, end=end))
df3 = pd.DataFrame(btcVBTPrice1.get('Close'))
df4 = pd.DataFrame(bctTAPrice1)

#Test printing
# print(df1)
# print(df2)
# print(df3)
# print(df4)

##So, we have shown a couple of ways to get historical data. Now, let's try to get some indicators

#First, with pandas-ta
#df4 is the dataframe with pandas-ta data
#Lets take a look at how df4 changes with the following operations

print(df4)
df4.ta.log_return(cumulative=True, append=True)
print(df4)
df4.ta.percent_return(cumulative=True, append=True)
print(df4)
df4.columns
df.tail(20)
print("")


