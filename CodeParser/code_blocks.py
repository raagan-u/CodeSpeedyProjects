tokens = {
	"\t": "tab_indent",
	"class": "class_def",
	"def": "func_def",
	"return": "ret",
}

def ret_tokens(input):
	try:
		if tokens[input]:
			return tokens[input]
	except KeyError as e:
			return None
