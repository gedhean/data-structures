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