"""
MQ MALA

accounts.py
"""

from account import *

class SavingAccount(Account):
	"""
	Creates a savings account
	"""
	def __init__(self, accountNumber, firstName, lastName, address, balance, minbalance):
		self.min_balance = minbalance
		
		Account.__init__(self, accountNumber, firstName, lastName, address, balance)
		
	def minBalance(self):
		"""
		post: return minimum balance
		"""
		return self.min_balance
	
class CurrentAccount(Account):
	"""
	Creates a current account
	"""
	def __init__(self, accountNumber, firstName, lastName, address, balance, interestrate):
		self.interestRate = interestrate
		
		Account.__init__(self, accountNumber, firstName, lastName, address, balance)
	
	def interetRate(self, interestrate):
		"""
		pre: takes interest rate
		post: sets interest rate
		"""	
		self.interestRate = interestrate
		
	def getInterestRate(self):
		"""
		post: return interest rate
		"""
		return self.interestRate		

# class