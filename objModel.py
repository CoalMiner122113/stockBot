class Stock:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
    #Getters
    def get_symbol(self):
        return self.symbol
    def get_name(self):
        return self.name
    
    ##Setters
    def set_symbol(self, symbol):
        self.symbol = symbol
    def set_name(self, name):
        self.name = name

class Transaction:
    def __init__(self, stock, action, quantity, price):
        self.stock = stock
        self.action = action
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.action}: {self.quantity} shares of {self.stock.symbol} at ${self.price:.2f} each"

class Portfolio:
    def __init__(self, starting_cash):
        self.stocks = {}
        self.transactions = []
        self.cash = starting_cash

    def add_stock(self, stock, quantity):
        symbol = stock.get_symbol()
        name = stock.get_name()

        if symbol in self.stocks:
            self.stocks[symbol]["quantity"] += quantity
        else:
            self.stocks[symbol] = {"name": name, "quantity": quantity, "price": 0}

    def remove_stock(self, stock, quantity):
        symbol = stock.get_symbol()
        
        if symbol not in self.stocks:
            raise ValueError(f"Stock {symbol} does not exist in the portfolio")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if quantity >= self.stocks[symbol]["quantity"]:
            del self.stocks[symbol]
        else:
            self.stocks[symbol]["quantity"] -= quantity

    def buy_stock(self, stock, quantity, price):
        symbol = stock.get_symbol()
        
        if symbol not in self.stocks:
            raise ValueError(f"Stock {symbol} does not exist in the portfolio")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        total_cost = price * quantity
        
        if total_cost > self.cash:
            raise ValueError("Not enough cash to complete transaction")
        
        self.cash -= total_cost
        self.stocks[symbol]["quantity"] += quantity
        self.stocks[symbol]["price"] = price
        self.transactions.append(Transaction(stock, "Buy", quantity, price))

    def sell_stock(self, stock, quantity, price):
        symbol = stock.get_symbol()
        
        if symbol not in self.stocks:
            raise ValueError(f"Stock {symbol} does not exist in the portfolio")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.stocks[symbol]["quantity"]:
            raise ValueError("Not enough shares to complete transaction")
        
        total_cost = price * quantity
        self.cash += total_cost
        self.stocks[symbol]["quantity"] -= quantity
        self.stocks[symbol]["price"] = price
        self.transactions.append(Transaction(stock, "Sell", quantity, price))
    
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)
    
    ##Getters
    def get_stocks(self):
        return self.stocks
    def get_transactions(self):
        return self.transactions
    def get_cash(self):
        return self.cash
    def get_value(self):
        value = self.cash
        for stock in self.stocks:
            value += self.stocks[stock]["quantity"] * self.stocks[stock]["price"]
        return value
    
