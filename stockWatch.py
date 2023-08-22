from datetime import datetime as dt
import yfinance as yf
import asyncio
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter = Limiter(RequestRate(2, Duration.SECOND*5)),
    bucket_class = MemoryQueueBucket,
    backend = SQLiteCache('yfinance.sqlite'),
)

async def current_price(ticker):
    return yf.Ticker(ticker, session = session).history(period='1d')['Close'][0]

#returns a moving average of a given ticker
async def moving_average(ticker, interval):
    #Get data from yfinance
    data = yf.Ticker(ticker, session = session).history(period='1d', interval=f'{interval}m')
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

asyncio.run(test())