# -*- coding: utf-8 -*-

"""
	Heap sort
"""

#create a max/min heap
def build_heap(tree, size, min_h=False):
	"""
		We don't try to sift_down things in leaf nodes 
		since they don't have children and no need to be sifted down anymore
		In a heap-tree the nodes which are not leaves always take an amount of
		floor(heap-size/2)
		So we'll try to build a heap-tree bottom-up from the lowest level non-leaf nodes
	"""
	for index in range(int(size/2-1),-1,-1):
		tree = sift_down(tree,index,size,min_h)

	return tree

#move the node at start position to an appropriate position on heap-tree
def sift_down(tree, start, size, min_h=False):
	#get index for nodes
	left = start*2+1
	right = start*2+2
	root = start

	#get the index of the largest/tiniest node among 3 nodes we got their indices
	if left<size:
		if min_h is False:
			root = left if tree[start] < tree[left] else start
		else:
			root = left if tree[start] > tree[left] else start
	if right<size:
		if min_h is False:
			root = right if tree[root] < tree[right] else root
		else:	
			root = right if tree[root] > tree[right] else root

	#recursively moving the start node to appropriate position
	if root!=start:
		temp = tree[start]
		tree[start] = tree[root]
		tree[root] = temp
		tree = sift_down(tree, root, size, min_h)

	return tree

def heap_sort(target, decrease = False):
	min_h = decrease #determine how to sort

	#memorize current in-processing size of tree-array
	size = len(target)

	#build heap the first time in full size of input-array
	target = build_heap(target, size, min_h)

	#run and process all node indices except for index at root
	for i in range(len(target)-1,0,-1):
		"""
			Switch the root of heap to the end of the array
			Since root of a heap must be largest/tiniest node in the tree,
			put that root to the very last leaf of the tree, so the largest/tiniest
			value will be at the end of the target array
		"""
		temp = target[i]
		target[i] = target[0]
		target[0] = temp

		#decrease the current in-processing size of tree by one 
		#(we won't touch the root which had been transfer to the end of array)
		size-=1

		#maintain the heap property for the array-tree without had-just-transfered root 
		target = sift_down(target, 0, size, min_h) #this will make the next largest/tiniest value comes to top of tree

	return target




if __name__ == '__main__':
	mode = input("Sort in numerical or lexicographical?(N/L): ").lower()
	
	target = input("Enter a list: ").split()
	
	if mode=="n":
		target = [int(x) for x in target]

	decr = input("Is this a decreasing sort? (Y/N): ").lower()
	decrease = True if decr =="y" else False

	print(heap_sort(target, decrease))