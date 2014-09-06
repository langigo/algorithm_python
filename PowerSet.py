# -*- coding: utf-8 -*-

"""
	Producing a Power set of a specific set of numbers
"""

def produce_subsets(target):
	powerset = [[]]
	for x in target:
		powerset+=[each + [x] for each in powerset]
	return powerset

if __name__ == '__main__':
	target = input("Enter a set of number: ").split()
	target = [int(term) for term in target]
	print(produce_subsets(target))