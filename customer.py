"""
MQ MALA

customer.py
"""

class Customer:
	"""
	Creates a bank customer
	"""
	def __init__(self, firstName, lastName, address):
		self.firstName = firstName
		self.lastName = lastName
		self.address = address
		
	def getFirstName(self):
		"""
		post: return first name
		"""
		return self.firstName
		
	def getLastName(self):
		"""
		post: return last name
		"""
		return self.lastName
		
	def getAddress(self):
		"""
		post: return address
		"""
		return self.address
