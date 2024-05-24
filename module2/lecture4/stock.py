class Stock:
    def __init__(self, iTicker, exchange, iPrice):
        self.ticker = iTicker
        self.exchange = exchange
        self.country = 'USA'
        self.price = iPrice
        self.dividend = 0.0

    def __repr__(self):
        return self.ticker + ' is listed on ' + self.exchange + ' and is based in ' + self.country
    
    def printYourself(self):
        template = f"I am representing a public equity in {self.ticker} listed on {self.exchange} and based in {self.country}"
        return template
    
    def update_price(self, new_price):
        self.price = new_price
        return self.price  

    def set_dividend(self, dividend):
        self.dividend = dividend
        if self.dividend < 0:
            print("Dividend cannot be negative. Setting dividend to 0.0")
            self.dividend = 0.0
        print("new dividend is: ", self.dividend)
        return self.dividend
    
    def calculateDividendYield(self):
        self.div_yield =  self.dividend / self.price
        print("Dividend yield is: ", self.div_yield)
        return self