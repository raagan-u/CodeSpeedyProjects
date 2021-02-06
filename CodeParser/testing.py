from codeparser import codeparser
lines = []
with open('sample_code.py') as fd:
	parser = codeparser()
	lines = list(fd)
parser.parse(lines[5])
parser.disp_one()
