import sys, code_blocks
class codeparser:
	_classes = []
	def __init__(self):
		print("parser object created")

	def parse(self,string):
		self.string = enumerate(string.split(" "))
		# print(string.split(" "))
		for i, j in self.string:
			if code_blocks.ret_tokens(j) == "func_def":
				codeparser._classes.append(string)

	def get_classes (self):
		return codeparser._classes

if __name__ == "__main__":
	with open(sys.argv[1]) as fd:
		lines = list(fd)
		parser = codeparser()
		for i in range(0,len(lines)):
			parser.parse(lines[i])
		print(parser.get_classes())
		print(*parser.get_classes())
