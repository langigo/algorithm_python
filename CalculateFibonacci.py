# -*- coding: utf-8 -*-

""" Calculate n-th Fibonacci number: 
	Based on matrix:
		[Fn+1   Fn]   [1   1] ^ n
		[Fn   Fn-1] = [1   0]
"""
def ma22_mult(a,b):
	result = [[0,0],
	          [0,0]]
	for i in range(2):
		for j in range(2):
			result[i][j] = a[i][0]*b[0][j]+a[i][1]*b[1][j]
	return result

def ma22_pow(matrix, n):
	result = [[1,0],
	          [0,1]]
	while n>0:
		if n%2==1:
			result = ma22_mult(result,matrix)
			n-=1
		else:
			matrix = ma22_mult(matrix,matrix)
			n/=2
	return result

def fib(n):
	if n==0: return 0
	l = abs(n)
	if l==1: return 1
	base_fib = [[1,1],
	            [1,0]]
	base_fib = ma22_pow(base_fib, l-1)
	fibo = base_fib[0][0]
	return fibo if n>0 else fibo*(-1)**((l+1)%2)

if __name__ == '__main__':
	print(fib(int(input("Which n-th fibonacci number??: "))))