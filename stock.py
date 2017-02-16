"""
This module creates classes for the stock object and the trade object 
which records trade of stock, also defines the get_geometric_mean function
to get the geometric mean from a list of stocks. Test with the test_stock_unittest
file which tests the stock.calc_yield, stock.calc_PE_ratio stock.calc_weighted_price 
and get_geometric_mean functions.

Written in Python 3.5, compatible with Python 2.7
"""

import datetime

class Trade(object):
	
	""" A class object that records a trade of stock. Takes arguments
	of the quantity, indicator and price and makes a timestamp when created."""
	
	def __init__(self, quantity, indicator, price):
		
		self.ts = datetime.datetime.now()
		self.quantity = quantity
		self.indicator = indicator
		self.price = price
		
	def __repr__(self):
		
		return "%s\t%s\t%s\t%s" %(self.quantity, self.indicator, self.price, self.ts)

class Stock(object):
	
	""" A class object for stocks, taking name, last dividend and par Value,
	setting the fixed dividend rate at none unless one is specified."""
	
	def __init__(self, name, last_dividend, par_value, fixed_dividend = ''):
		
		self.name = name
		self.last_dividend = last_dividend
		self.fixed_dividend = fixed_dividend
		self.par_value = par_value
		self.trades = []
		
	def calc_yield(self, price):
		
		return (float(self.last_dividend)/price)
		
	def calc_PE_ratio(self, price):      
		
		return (float(price)/self.calc_yield(price))
		
	def trade(self, quantity, indicator, price):
		""" Creates a new trade object then stores it in a list."""
		
		newTrade = Trade(quantity, indicator, price)
		self.trades.append(newTrade)
		
	def calc_weighted_price(self):
		""" Makes a list of all trades within last 900 seconds (15 mins)
		then returns weighted price of those trades."""
		
		recentTrades = []
		for trade in self.trades:
			if datetime.datetime.now() - trade.ts < datetime.timedelta(0, 900):
				recentTrades.append(trade)
	
		totalPrice = totalQty = 0
		for trade in recentTrades:
			totalPrice += trade.price * trade.quantity
			totalQty += trade.quantity
			
		self.price = totalPrice / totalQty
		
		return float(totalPrice) / totalQty	
	
	def __repr__(self):
		
		return "%s\t\t%s\t\t%s\t\t%s\t\t%s" % (self.name, self.__class__.__name__, self.last_dividend, self.fixed_dividend, self.par_value)
		
class Common(Stock):
	pass

class Preferred(Stock):
	
	""" Subclass for preferred stock which overloads the calc_yield func."""
	
	def calc_yield(self, price):
		return self.fixed_dividend * self.par_value / price
		


def get_geometric_mean(stocks):
	
	product = 1
	for stock in stocks:
		product *= stock.calc_weighted_price()
		
	return(product ** (1.0/len(stocks)))

