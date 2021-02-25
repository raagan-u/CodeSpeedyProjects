#!/usr/bin/python3
import sys
import tokenize

toks = {1:"NAME", 4:"NEWLINE", 5:"INDENT", 6:"DEDENT"}

ops = {"class": [] ,"funcs": []}
append_flag = 0
with open(sys.argv[1]) as fd:
	tokens = tokenize.generate_tokens(fd.readline)
	for i in tokens:
		if i.string == "def":
			append_flag = 1

		if append_flag == 1:
			ops["funcs"].append(i.line)
print(*(ops["funcs"]))
