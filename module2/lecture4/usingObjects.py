from stock import Stock

testStock = Stock("AAPL",'NYSE',16)

print(testStock.ticker)
print(testStock.exchange)

testStockTwo = Stock("GOOGL",'NASDAQ',51) 
print(testStockTwo.ticker)
print(testStockTwo.exchange)

testStockThree = Stock("AMZN",'NASDAQ',10)
testStockThree.country = 'RUS'
print(testStockThree.ticker)
print(testStockThree.exchange)
print(testStockThree.country)

print(testStock)
print(testStockTwo)
print(testStockThree)

print(testStock.printYourself())
testStock.set_dividend(-.05)
print(testStock.dividend)
testStock.set_dividend(.05)
print(testStock.dividend)

testStock.calculateDividendYield()
print(testStock.div_yield)
