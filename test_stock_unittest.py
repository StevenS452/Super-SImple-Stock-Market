import unittest
import stock

TEA = stock.Common("TEA", 1, 100)
POP = stock.Common("POP", 8, 100)
ALE = stock.Common("ALE", 23, 60)
GIN = stock.Preferred("GIN", 8, 100, 2)
JOE = stock.Common("JOE", 13, 250)
	
class StockTest(unittest.TestCase):
	
	def test_calc_yield(self):
		self.assertEqual(TEA.calc_yield(100), 0.01)
		self.assertEqual(POP.calc_yield(200), 0.04)
		self.assertEqual(ALE.calc_yield(230), 0.1)
		self.assertEqual(GIN.calc_yield(200), 1)
		self.assertEqual(JOE.calc_yield(130), 0.1)
		
	def test_calc_PE_ratio(self):
		self.assertEqual(TEA.calc_PE_ratio(100), 10000)
		self.assertEqual(POP.calc_PE_ratio(200), 5000)
		self.assertEqual(ALE.calc_PE_ratio(230), 2300)
		self.assertEqual(GIN.calc_PE_ratio(200), 200)
		self.assertEqual(JOE.calc_PE_ratio(130), 1300)
			
	def test_calc_weighted_price(self):
		TEA.trade(100, "BUY", 100)
		TEA.trade(100, "SELL", 200)
		POP.trade(200, "BUY", 100)
		POP.trade(200, "SELL", 200)
		ALE.trade(300, "BUY", 100)
		ALE.trade(300, "SELL", 120)
		GIN.trade(120, "BUY", 100)
		GIN.trade(240, "SELL", 250)
		JOE.trade(200, "BUY", 200)
		JOE.trade(100, "SELL", 350)
		print(TEA.trades)
		print(POP.trades)
		print(ALE.trades)
		print(GIN.trades)
		print(JOE.trades)
		self.assertEqual(TEA.calc_weighted_price(), 150)
		self.assertEqual(POP.calc_weighted_price(), 150)
		self.assertEqual(ALE.calc_weighted_price(), 110)
		self.assertEqual(GIN.calc_weighted_price(), 200)
		self.assertEqual(JOE.calc_weighted_price(), 250)
		
	def test_get_geometric_mean(self):		
		stocks = [TEA,POP,ALE,GIN,JOE]
		print(stock.get_geometric_mean(stocks))
		self.assertEqual(int(stock.get_geometric_mean(stocks)), 165)

	
if __name__ == '__main__':
	unittest.main()
