class stock:
    
    def __init__(self, ticker, price, entry, exit, numberOwned):
        self.ticker = ticker
        self.price = price
        self.entry = entry
        self.exit = exit
        self.numberOwned = numberOwned

    ##Relevant functions
    def buy(self, price, number):
        self.entry = price
        self.numberOwned = number
    
    def sell(self, price, number):
        self.exit = price
        self.numberOwned -= number
    
    def getProfit(self):
        return self.exit - self.entry
    
    ##Getters
    def getPrice(self):
        return self.price
    
    def getEntry(self):
        return self.entry
    
    def getExit(self):
        return self.exit
    
    def getNumberOwned(self):
        return self.numberOwned
    
    
    ##Setters
    def updatePrice(self, price):
        self.price = price
    
    def updateEntry(self, entry):
        self.entry = entry
    
    def updateExit(self, exit):
        self.exit = exit
            
class portfolio:
    
    def __init__(self, cashBalance, assetValue, day) :
        self.cashBalance = cashBalance
        self.assetValue = assetValue
        self.day = day
   
    ##Relevant functions
    def getTotalValue(self):
       return self.cashBalance + self.assetValue
   
    ##Getters 
    def getCashBalance(self):
        return self.cashBalance
    
    def getAssetValue(self):
        return self.assetValue
    
    def getDay(self):
        return self.day
    
    ##Setters, negative values for subtraction
    def setCashBalance(self, amount):
        self.cashBalance += amount
        
    def setAssetValue(self, amount):
        self.assetValue += amount
    
    def setDay(self, day):
        self.day = day