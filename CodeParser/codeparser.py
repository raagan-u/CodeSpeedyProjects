import sys
class codeparser:
	def __init__(self):
		print("parser object created"
		)
	def parse(self,string):
		self.string = enumerate(string.split(" "))
		print(string.split(" "))
	
	def disp_one(self):
		for i, j in self.string:
			print(i,'===>', j)

if __name__ == "__main__":
	with open(sys.argv[1]) as fd:
		parser = codeparser(fd)
		parser.parse()
