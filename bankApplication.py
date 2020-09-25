"""
MQ MAlA

bankApplication.py
"""

import bank
import csv

from readingFiles import *

def customerDB(filename, theBank):
	"""
	pre: enter a filename with the customer database
	post: return bank with customers
	"""
	# return list of customers
	customers = readCSVfile(filename)

	# add customer to the back
	for customer in customers:
		#print(customer.split(","))
		customerinfo = customer.split(",")
		#print(customerinfo[0])
		#print(customerinfo[1:])
		theBank.addAccount(customerinfo[1:], customerinfo[0])
	return "Uploaded successfully."

def getFileName():
	"""
	post: return file name
	"""
	return string(input("Enter here: "))

def selected():
	"""
	post: return option
	"""
	return int(input(""))

def menu(option):
	"""
	pre: get user option
	post: return next steps
	"""

	#initialize the bank
	theBank = bank.Bank()

	if option == 1:
		"""
		upload a file to update DB
		"""
		#file = getFileName()
		# file name with current information on bank customers
		fileName = 'customer.csv'
		customerDB(fileName, theBank)
	elif option == 2:
		"""
		get customer information
		"""
		print("Enter full name: ex. John Smith")
		name = getFileName()
		print("Enter address: ex. 9768 Fieldstone Rd. Bronx")
		address = getFileName()
		print("Enter state and zip: ex. NY 10456")
		address2 = getFileName()
		print("Enter saving amount: ex. $0.00 or -1 if not applicable")
		savings = selected()
		print("Enter current amount: ex. $0.00 or -1 if not applicable")
		current = selected()

	elif option == 3:
		"""
		remove account
		"""
		# get input from user
		print("Enter the account number")
		acctNum = getFileName()
		print("delete: \n\t- S for savings\n\t- C for current\n\t- A for account")
		whatToDelete = getFileName()

		# remove the account
		try:
			theBank.removeAccount(acctNum, whatToDelete)
			print("Completed.")
		except:
			print("Account number does not exist")
	elif option == 4:
		 pass
	elif option == 5:
		pass
	elif option == 6:
		pass
	elif option == 7:
		print("Goodbye!")
		quit()

def main():
	"""
	Run the application
	"""

	# menu 
	message = "1. Upload file\n2. Add customer\n3. Remove Customer\n"
	message1 = "4. Deposit\n5. Withdraw\n6. Show balance\n7. Exit"
	print(message + message1) 
	option = selected()
	assert 0 < option < 8
	menu(option)

if __name__ == '__main__':
	main()