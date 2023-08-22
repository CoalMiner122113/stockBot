import asyncio
import stockWatch
import objModel



async def btcStrat():
    
    ##Create a portfolio with $100,000
    testPortfolio = objModel.Portfolio(100000)
    ##Create a stock object for BTC
    btc = objModel.Stock('BTC-USD', 'Bitcoin')
    ##Add BTC to the portfolio watchlist
    testPortfolio.add_stock(btc, 0)
    ##Start a loop counter
    loopCount = 0
    ##Get the initial rating of BTC
    old_rating = (await stockWatch.compareMA(btc.get_symbol()))["Rating"]
    print(f"Initial Rating: {old_rating}")
    
    ##While loop runs until the portfolio runs out of cash and assets
    while testPortfolio.get_value() > 0:
        
        
        ##Wait 2 minutes before checking again
        await asyncio.sleep(2 * 60)
        
        ##Print the loop count        
        print(f"Loop {loopCount}")
        loopCount += 1
        
        ##Get the new rating of BTC
        new_rating = (await stockWatch.compareMA(btc.get_symbol()))["Rating"]
        
        ##If the rating has changed, print the new rating and take action
        if old_rating != new_rating:
        
            print(f"New Rating: {new_rating}")
            
            ##If the rating is buy, use 75% of the cash in the portfolio to buy BTC
            if new_rating == "Buy!":
                price = (await stockWatch.current_price(btc.get_symbol()))
                quantity = testPortfolio.get_cash() * .75 / price
                testPortfolio.buy_stock(btc, quantity, price)
                print(testPortfolio.get_stocks())
            
            ##If the rating is sell, sell all BTC in the portfolio
            elif new_rating == "Sell!":
                if testPortfolio.get_stocks()[btc.get_symbol()]["quantity"] == 0:
                    print("No BTC to sell!")
                    continue
                price = (await stockWatch.current_price(btc.get_symbol()))
                quantity = testPortfolio.get_stocks()[btc.get_symbol()]["quantity"]
                testPortfolio.sell_stock(btc, quantity, price)
                print(testPortfolio.get_stocks())
            
            ##If the rating is hold, do nothing
            else:
                print("Hold!")
            
            ##Update old rating
            old_rating = new_rating
    
    ##End of while loop            
    print("Out of cash!")
    testPortfolio.display_transactions()
    


def testObjModel():
    
    ##Create a portfolio with $100,000 
    testPortfolio = objModel.Portfolio(100000)
    
    ##create a stock object for BTC and add it to the portfolio watchlist
    btc = objModel.Stock('BTC-USD', 'Bitcoin')
    testPortfolio.add_stock(btc, 0)
        
    ##Buy 1 BTC at $50,000
    testPortfolio.buy_stock(btc, 1, 50000)
    
    ##Check the portfolio value
    print("Cash Value: ", testPortfolio.get_cash())
    print("Portfolio Value: ", testPortfolio.get_value())
    
    
    ##Sell 1 BTC at $60,000
    testPortfolio.sell_stock(btc, 1, 60000)
    
    ##Check the portfolio value
    print("Cash Value: ", testPortfolio.get_cash())
    print("Portfolio Value: ", testPortfolio.get_value())

asyncio.run(btcStrat())
#testObjModel()