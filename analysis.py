import pandas as pd
import pandas_ta as ta
import yfinance as yf
import vectorbt as vbt


##How to get last 3 years of daily data on Apple
# ticker = yf.Ticker("AAPL")
# df = pd.DataFrame(ticker.history(period="36mo"))
# print(df)

df = pd.DataFrame().ta.ticker("AAPL") # requires 'yfinance' installed
# Create the "Golden Cross" 
df["GC"] = df.ta.sma(50, append=True) > df.ta.sma(200, append=True)

# Create boolean Signals(TS_Entries, TS_Exits) for vectorbt
golden = df.ta.tsignals(df.GC, asbool=True, append=True)

# Sanity Check (Ensure data exists)
print(df.get("Close"))

# Create the Signals Portfolio
pf = vbt.Portfolio.from_signals(df.get("Close"), entries=golden.TS_Entries, exits=golden.TS_Exits, freq="D", init_cash=100_000, fees=0.0025, slippage=0.0025)

# Print Portfolio Stats and Return Stats
print(pf.stats())
print(pf.returns_stats())

