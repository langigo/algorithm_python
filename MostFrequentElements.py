# -*- coding: utf-8 -*-

"""
	A small solution for finding all most frequently appearred items in a list of items
"""

def find_most_freq(target):
	#get a count for all elements
	counters = {x:target.count(x) for x in target}

	#produce array of the most frequent elements
	result = [x for x in counters if counters[x]==max(counters.values())]
	return result

if __name__ == '__main__':
	anythings = input("Enter somethings: ").split()
	print(find_most_freq(anythings))