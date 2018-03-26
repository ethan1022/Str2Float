# -*- coding: utf-8 -*-
from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
	def fn(x, y):
		return x * 10 + y
	n = len(s) - s.index('.') - 1 #find the index of . char from backward
	newS = s.replace('.', '') #replace . to ''
	def char2Num(s):
		return digits[s]
	return reduce(fn, map(char2Num, newS)) / (10**n)

print(str2float('123.4567')) #test