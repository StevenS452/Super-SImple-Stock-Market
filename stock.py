import datetime

class Trade:
	
	""" A class object that records a trade of stock. Takes arguments
	of the quantity, indicator and price and makes a timestamp when created."""
	
	def __init__(self, quantity, indicator, price):
		
		self.ts = datetime.datetime.now()
		self.quantity = quantity
		self.indicator = indicator
		self.price = price
		
	def __repr__(self):
		
		return "%s\t%s\t%s\t%s" %(self.quantity, self.indicator, self.price, self.ts)

class Stock:
	
	""" A class object for stocks, taking name, last dividend and par Value,
	setting the fixed dividend rate at none unless one is specified."""
	
	def __init__(self, name, lastDividend, parValue, fixedDividend = ''):
		
		self.name = name
		self.lastDividend = lastDividend
		self.fixedDividend = fixedDividend
		self.parValue = parValue
		self.trades = []
		
	def calcYield(self, price):
		
		return self.lastDividend/price
		
	def calcPEratio(self, price):      
		
		return price/self.calcYield(price)
		
	def trade(self, quantity, indicator, price):
		""" Creates a new trade object then stores it in a list."""
		
		newTrade = Trade(quantity, indicator, price)
		self.trades.append(newTrade)
		
	def calcWeightedPrice(self):
		""" Makes a list of all trades within last 900 seconds (15 mins)
		then returns weighted price of those trades."""
		
		recentTrades = []
		for trade in self.trades:
			if datetime.datetime.now().timestamp() - trade.ts.timestamp() < 900:
				recentTrades.append(trade)
	
		totalPrice = totalQty = 0
		for trade in recentTrades:
			totalPrice += trade.price * trade.quantity
			totalQty += trade.quantity
			
		self.price = totalPrice / totalQty
		
		return totalPrice / totalQty	
	
	def __repr__(self):
		
		return "%s\t\t%s\t\t%s\t\t%s\t\t%s" % (self.name, self.__class__.__name__, self.lastDividend, self.fixedDividend, self.parValue)
		
class Common(Stock):
	pass

class Preferred(Stock):
	
	""" Subclass for preferred stock which overloads the calcYield func."""
	
	def calcYield(self, price):
		return self.fixedDividend * self.parValue / price
		


def getGeometricMean(stocks):
	
	product = 1
	for stock in stocks:
		product *= stock.calcWeightedPrice()
		
	return(product ** (1/len(stocks)))



def test():

	stocks = []
	stocks.append(Common("TEA", 1, 100))
	stocks.append(Common("POP", 8, 100))
	stocks.append(Common("ALE", 23, 60))
	stocks.append(Preferred("GIN", 8, 100, 2))
	stocks.append(Common("JOE", 13, 250))
	
	print("Dividend yield for price = 100: \n")
	for stock in stocks:
		print(stock.calcYield(100))
	
	print("\nP/E ratio for price = 100:\n")
	for stock in stocks:
		print(stock.calcPEratio(100))
		
	print("\nTrading:\n")
	for stock in stocks:
		print(stock.name)
		stock.trade(100, "BUY", 100)
		stock.trade(200, "SELL", 110)
		for trade in stock.trades:
			print(trade)
			
	print("\nWeighted prices:\n")	
			
	for stock in stocks:
		print(stock.calcWeightedPrice())

	print("\nGBCE All Share Index: ", getGeometricMean(stocks), "\n")

		
if __name__ == "__main__":
		
	test()
