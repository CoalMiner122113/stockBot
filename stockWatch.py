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
async def moving_average(ticker, interval):
    #Get data from yfinance
    data = yf.Ticker(ticker).history(period='1d', interval=f'{interval}m')
    #Calculate moving average
    data['MA'] = data['Close'].rolling(window = 5).mean()
    #Return the last value of the moving average
    return data['MA'][-1]

##Compares a slow and fast moving average
##If the fast moving average crosses above the slow moving average, it returns a buy signal
##If the fast moving average crosses below the slow moving average, it returns a sell signal
async def compareMA(ticker):
    slowMA_Interval = 5
    fastMA_Interval= 1

    slowMA = (await moving_average(ticker, slowMA_Interval))
    fastMA = (await moving_average(ticker, fastMA_Interval))
    
    ret = {"Rating": "Undertermined", 
           "Fast MA": fastMA, 
           "Slow MA": slowMA}
    
    if fastMA > slowMA:
        ret["Rating"] = "Buy!"
    elif fastMA < slowMA:
        ret["Rating"] = "Sell!"
    else:
        ret["Rating"] = "Hold!"
    
    return ret

async def test():
    print("Hello World")
    ret = await compareMA('BTC-USD')
    rating = ret["Rating"]
    fastMA = ret["Fast MA"]
    slowMA = ret["Slow MA"]
    print(f'Rating: {rating}\nFast MA: {fastMA}\nSlow MA: {slowMA}')

#asyncio.run(test())