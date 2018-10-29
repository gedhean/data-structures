from math import ceil

def merge(array, start, mid, end):
	if not (end < len(array)):
		return
	aux = array.copy()
	j, left, right = start, start, mid
	
	# Merge the two arrays until overflow one of them
	while left < mid and right <= end:
		if aux[left] > aux[right]:
			array[j] = aux[right]
			right += 1
		elif aux[left] <= aux[right]:
			array[j] = aux[left]
			left += 1
		j += 1
	# Copy the rest of left array in case of right array overflow
	while left < mid:
		array[j] = aux[left]
		left = left + 1
		j += 1
	# Copy the rest of right array in case of left array overflow
	while right <= end:
		array[j] = aux[right]
		right += 1
		j += 1

def merge_sort(array):
	start = 0
	end = len(array) - 1

	def _merge_sort(array, start, end):
		mid = ceil((end + start)/2)
		if (start < end):
			_merge_sort(array, start, mid - 1)
			_merge_sort(array, mid, end)
			merge(array, start, mid, end)

	_merge_sort(array, start, end)

def merge_sort_i(array):	
	block = 1
	arraySize = len(array)
	while block < arraySize:
		mid = block
		start = 0
		end = mid + block - 1
		while mid < arraySize:
			merge(array, start, mid, min(end, arraySize - 1))
			start = end + 1
			mid = end  + block + 1
			end = mid + block - 1
		block *= 2 

def is_sorted(array):
	'''
	Return true if the given array is sorted ascending
	type array: list
	rype: boolean
	'''
	minElement = float("-inf")
	for element in array:
		if minElement > element:
			return False	
		minElement = element
	return True

if __name__ == '__main__':
	from random import sample

	for s in range(1,11):
		print('Merge Sort random test -', s)		
		arr = sample(range(100), 10)
		print(arr, " is sorted? ", is_sorted(arr))
		merge_sort_i(arr)
		print(arr, " is sorted? ", is_sorted(arr))
		print('\n')