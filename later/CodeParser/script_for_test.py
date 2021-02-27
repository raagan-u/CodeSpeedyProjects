#!/usr/bin/python3
def user_def1(a, b , c):
	print("get something")
	if 10 == 10:
		yield 20
	else:
		return 30
	return 24

class Sample:
	class_var = "test"
	def __init__(self):
		print("init called")
	
	def sum(self):
		print("some_rand_func")
		return 1,2,"test"
	def __del__(self):
		print('sayanora')

for i in range(0,10):
	if i%2 == 0:
		print("something")
