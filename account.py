"""
MQ MALA

account.py
"""

import customer

from datetime import datetime

class Account:
	"""
	Parent class for bank account
	"""
	
	def __init__(self, accountNumber, firstName, lastName, address, balance):
		self.accountNumber = accountNumber
		self.balance = balance
		self.customer = self.addCustomer(firstName, lastName, address)
		self.Date_of_opening = self.dateOfOpening()
		
	def debitAmount(self, amount):
		"""
		pre: take amount
		post: adds amount to balance
		"""
		self.balance += amount
		
	def creditAmount(self, amount):
		"""
		pre: take amount
		post: subtract amount from balance
		"""
		self.balance -= amount
		
	def getAccountNumber(self):
		"""
		post: return account number
		"""
		return self.accountNumber
		
	def getBalance(self):
		"""
		post: return current balance
		"""
		return self.balance
		
	def addCustomer(self, firstName, lastName, address):
		"""
		pre: takes first and last name, and address
		post: returns customer object
		"""
		return customer.Customer(firstName, lastName, address)
			
	def removeCustomer(self, accountNumber):
		"""
		pre: takes account number
		post: returns null
		"""
		if self.accountNumber == accountNumber:
			self.customer = null
			
	def dateOfOpening(self):
		"""
		post: set date of opening
		"""
		now = datetime.now()
		
		self.Date_of_opening = now.strftime("%m/%d/%Y %H:%M:%S")
		
	def getDateOfOpening(self):
		"""
		post: return date account is opened
		"""
		return self.Date_of_opening
		
	def getCustomer(self):
		"""
		post: return customer name and address
		"""
		customer = self.customer.getFirstName() + ' ' + self.customer.getLastName() + ' ' + self.customer.getAddress()
		return customer

	def getAccountInfo(self):
		"""
		post: return account number, date opened and balance
		"""
		return 'Account number: ' + self.getAccountNumber() + '\nDate of Opening: ' + self.getDateOfOpening() + '\nCurrent balance: $' + self.getBalance() 
	
