"""
testBankApplication.py
"""

import unittest

from accounts import SavingAccount, CurrentAccount
from bank import *

class TestBankApplication(unittest.TestCase):

	def testGetBalance4Savings(self):
			sC = SavingAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 100.00)
			
			self.assertEqual(sC.getBalance(), 43.33, 'Should be 43.33')
			
	def testGetCustomer(self):
			sC = SavingAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 100.00)
			
			self.assertEqual(sC.getCustomer(), "MQ Mala 2550 Waverly Iowa MN 55103", 'Should be MQ Mala 2550 Waverly Iowa MN 55103')
			
	def testGetBalance4Current(self):
			cC = CurrentAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 4.5)
			
			self.assertEqual(cC.getBalance(), 43.33, 'Should be 43.33')
			
	def testDebitAmount(self):
			cC = CurrentAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 4.5)
			cC.debitAmount(50.00)
			self.assertEqual(cC.getBalance(), 93.33, 'Should be 93.33')
			
	def testGetAccountNumber(self):
		cC = CurrentAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 4.5)
		
		self.assertEqual(cC.getAccountNumber(), 'mala6453', 'Should be mala6453')
			
	def testAddAccount(self):
		cC = CurrentAccount("mala6453", "MQ", "Mala", "2550 Waverly Iowa MN 55103", 43.33, 4.5)
		newAccount = Bank()
		newAccount.addAccount(cC, cC.getAccountNumber())
		
		self.assertEqual(newAccount.getAccount('mala6453').getBalance(), 43.33,'Should be 43.33')
		

if __name__ == '__main__':
	unittest.main()
