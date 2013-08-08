#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class FooparseTypeError(Exception):
	pass

# from $somefoo(1, 10.5, 'test str') returns 'somefoo'
def getFooName(e):
	if e[0] != '$':
		return ''
	else:
		return e[1:e.index('(')]

# from $somefoo(1, 10.5, 'test str') returns (1, 10, 'test str')
def fooParse(e):
	def isFloat(string):
		try:
			float(string)
			return True
		except ValueError:
			return False
	lbracket_ind = e.index('(')
	raw_foo_args = e[lbracket_ind+1:-1].split(',')
	foo_args = []
	for arg in raw_foo_args:
		arg = arg.strip()
		if arg == '':
			pass
		elif arg.isdigit():
			foo_args.append(int(arg))
		elif (isFloat(arg)):
			foo_args.append(float(arg))
		elif (arg[0] == arg[-1] == '"') or (arg[0] == arg[-1] == "'"): # string
			foo_args.append(arg[1:-1])
		else:
			raise matsts_exception.FooparseTypeError()
	return tuple(foo_args)
