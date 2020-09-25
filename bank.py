"""
MQ MALA

bank.py
"""

import random

from accounts import *
from account import *

class Bank:
	"""
	Creates a bank with customers
	"""
	
	def __init__(self):
		self.name = "MALA investment bank"
		self.address = "PO 100 Simunye Swaziland L301"
		self.accounts = {}
		
	def getAddress(self):
		"""
		post: return address
		"""
		return self.address
		
	def setAddress(self, address):
		"""
		pre: takes address
		post: sets address
		"""
		self.address = address
		
	def getName(self):
		"""
		post: return bank name
		"""
		return self.name
		
	def setName(self, bankName):
		"""
		pre: takes bank name
		post: sets bank name
		"""
		self.name = bankName
		
	def addAccount(self, account, accountNumber):
		"""
		pre: takes a account and account number
		post: adds account to bank
		"""
		if self.accountNumberExists(accountNumber) == False:
			self.accounts[accountNumber] = account
			return "added."

		return "Cannot override account number"
		
	def removeAccount(self, accountNumber, accountType='a'):
		"""
		pre: takes account number and account type
		post: deletes account type for matching account number
		
		s - savings account
		c - current account
		a - all account
		"""
		for key, value in self.accounts.items():
			if key == accountNumber:
				if accountType == 's':
					del self.accounts[accountNumber]['s']
				elif accountType == 'c':
					del self.accounts[accountNumber]['c']
				elif accountType == 'a':
					del self.accounts[accountNumber]
					
	def getAccount(self, accountNumber):
		"""
		pre: takes account number
		post: return the account related to the account number
		"""
		return self.accounts.get(accountNumber)

	def accountNumberExists(self, accountNumber):
		"""
		pre: get account number
		post: return true if account is in database
		"""
		idExist = self.getAccount(accountNumber)
		if idExist != None:
			return True

		return False 


	def accountNumberGenerator(self, BankName=None):
		"""
		pre: get bank name
		post: return account number
		"""
		if BankName == None:
			BankName = self.getName()
		number = []
		while len(number) < 4:
			number.append(chr(random.randrange(65, 90, 1)))
		
		while len(number) < 11:
			# random.randrange(47,57,1)
			number.append(chr(random.randrange(48, 57, 1)))

		return BankName[:4] + "".join(number)

	def newMember(self, name, address1, address2, savings, current):
		"""
		pre: taking information for a new member
		"""
		pass