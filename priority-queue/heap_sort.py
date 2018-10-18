from max_heap import heapfy, extractMax, strIntegerListToArray

def heapSort(array):
	'''
	Sort the given array in-place (asc).
	type array: list
	'''
	# Build a max heap
	heapfy(array)
	# Extract max and put at the end of the array
	# Call it again for array lenght - 1, array lenght - 2, and so on 
	for index in range(len(array), 0, -1):
		extractMax(array, end=index)

def main():
	array = strIntegerListToArray()
	print(array)
	heapSort(array)
	print(array)

if __name__ == '__main__':
	main()