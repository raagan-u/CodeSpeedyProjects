#!/usr/bin/python3
import sys, tokenize, re

if len(sys.argv) < 2:
	print(sys.argv[0], " <script>")
	sys.exit(-1)

file_name = sys.argv[1]
funcs, classes = [], []
INDENT, DEDENT = 5, 6
NAME, NEWLINE, NL = 1, 4, 61 
append_flag = 0
with open(file_name, "r") as fd:
	tokens = list(tokenize.generate_tokens(fd.readline))
	for i in tokens:
		tab_num = 0
		tab = re.finditer(r'\t', i.line)
		for i in tab:
			tab_num = i.span()[-1]
		if new_tab_count > tab_num:
			if i.string == "def":
				append_flag = 1
		
			if append_flag:
				if i.line not in funcs:
					funcs.append(i.line)
		
			if i.string[0:0] != "\t":
				append_flag = 0
print(*funcs)
