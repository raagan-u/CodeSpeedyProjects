#PyStockExchange
class Member:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name} is I don't have a single idea"

class Remiser:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name} is an agent for The Member of SE"

class Broker:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name} is a Commission Agent, intermediates b/w sellers and buyers"

class Auth_Clerk:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name} is an Employee of The Members"

class Jobber:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name} is a Security Merchant"

class Speculators:
	def _init__(self):
		self.type = ['bull', 'bear', 'stag', 'lame_duck']
		print(self.type)

if __name__ == '__main__':
	mr_x = Remiser("mr_x")
	mr_y = Broker("mr_y")
	mr_z = Jobber("mr_z")
	print(mr_y, mr_z, sep="\n")
	print(mr_x)
