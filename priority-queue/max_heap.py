def maxHeap(array, index):
	'''
	Move the element at the given index (1-base index) to achive the max-heap inveriant.
	type array: list
	type index: integer
	rtype: void
	'''
	lastIndex = len(array)
	# Empty array
	if lastIndex == 0:
		return
	leftChildIndex = index * 2
	rightChildIndex = leftChildIndex + 1
	# element is a leaf
	if leftChildIndex > lastIndex or rightChildIndex > lastIndex:
		return
	# initialize with -infinity
	leftValue = rightValue = -float('inf')
	if leftChildIndex <= lastIndex:
		# array is 0-based index so need to decrese 1
		leftValue = array[leftChildIndex-1]
	if rightChildIndex <= lastIndex:
		# array is 0-based index so need to decrese 1
		rightValue = array[rightChildIndex-1]
	
	childIndex = leftChildIndex if leftValue > rightValue else rightChildIndex
	if array[index-1] < array[childIndex-1]:
		temp = array[index-1]
		array[index-1] = array[childIndex-1]
		array[childIndex-1] = temp
		maxHeap(array, childIndex)

def heapfy(array):
	from math import floor
	# maxHeap just half of the elements, the rest are leafs
	n = floor(len(array)/2)
	# bottom-up approach
	for index in range(n, 0, -1):
		maxHeap(array, index)

def extractMax(max_heap, end=None):
	'''
	By the truth, just move max to the end position in the max-heap
	'''
	heap_size = len(max_heap) 
	if end > heap_size:
		raise ValueError('Param end exceed heap size!')
	if end is None:
		end = heap_size
	if max_heap:
		temp = max_heap[0]
		max_heap[0] = max_heap[end-1]
		max_heap[end-1] = temp
		siftDown(max_heap, index=1, end=end-1)

def siftDown(max_heap, index, end=None):
	'''
	Used to keep the max-heap invariant.
	Parent >= children
	'''
	if end is None:
		end = len(max_heap)
	parent = index
	left = index * 2
	right = left + 1
	if right <= end: 	# has two children
		child = left if max_heap[left-1] > max_heap[right-1] else right
	elif left <= end: 	# has only left child
		child = left
	else:				# is a leaf
		return

	while child <= end and max_heap[parent-1] < max_heap[child-1] :
		temp = max_heap[parent-1]
		max_heap[parent-1] = max_heap[child-1]
		max_heap[child-1] = temp
		parent = child
		left = parent * 2
		right = left + 1
		if right <= end:
			child = left if max_heap[left-1] > max_heap[right-1] else right
		elif left <= end:
			child = left
		else:
			break


def strIntegerListToArray():
	'''
	Receive a comman separeted list of integer from the user and a list of the given integers
	rtype: list
	'''
	strInput = input('Digit a list of integers separeted by comman: ')
	srtList = strInput.split(',')
	result = []
	for char in srtList:
		if char.isnumeric():
			result.append(int(char))
	return result

def main():
	arr = [2,3,4,1,0]
	print('Array test 1: ',arr)
	maxHeap(arr, 1)
	print('Max heapfied: ',arr)

	arr2 = [1,2,3,4,5,6,7]
	print('Array test 2: ',arr2)
	heapfy(arr2)
	print('Max heapfied: ',arr2)

	arr3 = strIntegerListToArray()
	print('Array test 3: ',arr3)
	heapfy(arr3)
	print('Max heapfied: ',arr3)
	

if __name__ == '__main__':
	main()