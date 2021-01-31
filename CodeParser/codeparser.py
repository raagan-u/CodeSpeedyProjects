import sys
def codeparser(string):
	key = string.split(" ")
	print(key)

if __name__ == "__main__":
	with open(sys.argv[1]) as fd:
		for i in fd:
			codeparser(i)
