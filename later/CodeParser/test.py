#!/usr/bin/python3
import sys, tokenize, re

fd = open(sys.argv[1], 'r')
tokens = tokenize.generate_tokens(fd.readline)

def get_tab_num(string):
	ret_tab = 0
	tab_temp = re.finditer(r'\t', string)
	for i in tab_temp:
		ret_tab = i.span()[-1]
	return ret_tab

funcs = []
append_flag = 0

for token in tokens:
	if token.string == "def":
		append_flag = 1
		def_indent = get_tab_num(token.line)
		if token.line not in funcs:
			funcs.append(token.line)
	
	curr_tab = get_tab_num(token.line)
	if append_flag == 1:
		if token.string != "def":
			if curr_tab > def_indent:
				if token.line not in funcs:
					funcs.append(token.line)
			else:
				append_flag = 0
fd.close()
print(*funcs)
