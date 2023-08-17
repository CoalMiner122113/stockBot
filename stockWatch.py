import numpy as np
import pandas as pd
from datetime import datetime as dt
import vectorbt as vbt
import yfinance as yf
import pandas_ta as ta
import asyncio

async def current_price(ticker):
    return yf.Ticker(ticker).history(period='1d')['Close'][0]

#returns a moving average of a given ticker
async def moving_average(ticker, period):
    #Get data from yfinance
    data = yf.Ticker(ticker).history(period='1d', start='2020-01-01', end=dt.now())
    #Calculate moving average
    data['MA'] = data['Close'].rolling(period).mean()
    #Return the last value of the moving average
    return data['MA'][-1]

##Compares a slow and fast moving average
##If the fast moving average crosses above the slow moving average, it returns a buy signal
##If the fast moving average crosses below the slow moving average, it returns a sell signal
async def compareMA(ticker):
    slowMA_Interval = 100
    fastMA_Interval= 10

    slowMA = (await moving_average(ticker, slowMA_Interval))
    fastMA = (await moving_average(ticker, fastMA_Interval))
    
    if fastMA > slowMA:
        return "Buy!" + "\nFast MA: " + str(fastMA) + "\nSlow MA: " + str(slowMA)
    elif fastMA < slowMA:
        return "Sell!" + "\nFast MA: " + str(fastMA) + "\nSlow MA: " + str(slowMA)
    else:
        return "Hold"

response = compareMA('BTC-USD')
print(response)