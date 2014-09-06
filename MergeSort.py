# -*- coding: utf-8 -*-

"""
Idea of merge sort:
	_Recursively split unsorted list into 2 sub-list, split until each sub-lists has only 1 memeber
	_For each 2 sub-lists, join them together by comparing 2 first members of 2 sub-lists, and append to the result-list of the join
"""

#implementation: acceptance parameter is a list
def merge_sort(target, decrease=False):
	if len(target)<=1:
		return target
	
	#center of the list
	mid_index = int(len(target)/2)

	#divine into 2 sub-lists
	sub_left = target[:mid_index]
	sub_right = target[mid_index:]

	#recursively sort sub-list
	sub_left = merge_sort(sub_left, decrease)
	sub_right = merge_sort(sub_right, decrease)

	#merge sorted sub-lists
	return merging(sub_left, sub_right, decrease)


def merging(sleft, sright, decr):
	combine = []
	while len(sleft)>0 or len(sright):
		if len(sleft)>0 and len(sright)>0:
			if decr is False:
				combine.append(sleft.pop(0) if sleft[0]<=sright[0] else sright.pop(0))	
			else:
				combine.append(sleft.pop(0) if sleft[0]>=sright[0] else sright.pop(0))
		else:
			combine+=sleft+sright
			break
	return combine

if __name__ == '__main__':
	mode = input("Sort in numerical or lexicographical?(N/L): ").lower()
	
	target = input("Enter a list: ").split()
	
	if mode=="n":
		target = [int(x) for x in target]

	decr = input("Is this a decreasing sort? (Y/N): ").lower()
	decrease = True if decr =="y" else False

	print(merge_sort(target, decrease))