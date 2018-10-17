from math import floor

class BinaryMaxHeap:
	"""Represent a Binary Max Heap"""
	def __init__(self, maxSize):
		self.heap = [None] * maxSize
		self.size = 0 
		self.maxSize = maxSize
	
	def getValue(self, index):
		'''
		Get the value of the given index in the BinaryMaxHeap
		rtype: integer
		'''
		if self.size != 0 and index <= self.size:
			return self.heap[index - 1]
		raise ValueError('Could not get value. Index out of range.')

	def setValue(self, index, value):
		'''
		Set the value of the given index in the BinaryMaxHeap
		'''
		if index > self.size and index < 1:
			raise ValueError('Could not set value. Invalid index.')
		self.heap[index - 1] = value

	def insert(self, value):
		'''
		Insert the given value in the BinaryMaxHeap
		type value: integer
		rtype: void
		'''
		# heap is full
		if self.size >= self.maxSize:
			raise ValueError('Could not insert. Heap if full!')
		# Empty heap
		if self.isEmpty():
			print('First heap element')
			self.setValue(1, value)
			self.size += 1
		else:
			index = self.size + 1
			self.setValue(index, value)
			self.size += 1
			self.siftUp(index)

	def extractMax(self):
		'''
		Return and delete the max value from the BinaryMaxHeap.
		rtype: integer
		'''
		return self.remove(1)

	def remove(self, index):
		'''
		Remove and return the value of given index from the BinaryMaxHeap.
		rtype: integer or None
		'''
		if index > self.getSize():
			raise ValueError('Could not remove. Index out of range!')
		if self.isEmpty():
			return None
		lastIndex = self.size
		value = self.getValue(index)
		self.swapValues(index, lastIndex)
		self.setValue(lastIndex, None)
		self.size -= 1
		self.siftDown(index)
		return value

	def siftUp(self, index):
		'''
		Move up an element value in the BinaryMaxHeap to keep truly the max heap inveriant:
		Parent value >= children values
		type index: integer
		rtype: void 
		'''
		childIndex = index
		parentIndex = self.getParentIndex(index)
		while self.getValue(parentIndex) < self.getValue(childIndex):
			self.swapValues(parentIndex, childIndex)
			childIndex = parentIndex
			parentIndex = self.getParentIndex(childIndex)

	def siftDown(self, index):
		'''
		Move down an element value in the BinaryMaxHeap to keep truly the max heap inveriant:
		Parent value >= children values
		type index: integer
		rtype: void 
		'''
		parentIndex = index
		rightChildIndex = self.getRightChildIndex(parentIndex)
		leftChildIndex = self.getLeftChildIndex(parentIndex)
		if rightChildIndex > self.size:
			return
		childIndex = leftChildIndex if self.getValue(leftChildIndex) > self.getValue(rightChildIndex) else rightChildIndex

		while (childIndex < self.size) and (self.getValue(parentIndex) < self.getValue(childIndex)):
			
			self.swapValues(parentIndex, childIndex)
			parentIndex = childIndex
			rightChildIndex = self.getRightChildIndex(parentIndex)
			leftChildIndex = self.getLeftChildIndex(parentIndex)
			if rightChildIndex > self.size:
				break
			childIndex = leftChildIndex if self.getValue(leftChildIndex) > self.getValue(rightChildIndex) else rightChildIndex
	
	def swapValues(self, index1,index2):
		'''
		Swap two values in the BinaryMaxHeap
		type index1: integer
		type index2: integer
		rtype: void
		'''
		temp = self.getValue(index1)
		self.setValue(index1, self.getValue(index2)) 
		self.setValue(index2, temp)

	def getParentIndex(self, index):
		'''
		Retrun the parent index of the given elment index.
		type index: integer
		rtype: integer
		'''
		if index == 1: 
			return 1
		return floor(index/2)

	def getLeftChildIndex(self, index):
		'''
		Return the Left Child index of the given element index.
		type index: integer
		rtype: integer
		'''
		return (2 * index)

	def getRightChildIndex(self, index):
		'''
		Return the Right Child index of the given element index.
		type index: integer
		rtype: integer
		'''
		return ((2 * index) + 1)

	def isEmpty(self):	
		'''
		Return True if the BinaryMaxHeap is empty or False otherwise.
		rtype: bool
		'''
		return self.size == 0

	def isFull(self):	
		'''
		Return True if the BinaryMaxHeap is full or False otherwise.
		rtype: bool
		'''
		return self.size == self.maxSize

	def getMax(self):
		'''
		Return the max value in the BinaryMaxHeap.
		rtype: integer or None
		'''
		if self.isEmpty():
			return None
		return self.getValue(1)

	def getSize(self):
		'''
		Return the number of elements in the BinaryMaxHeap
		rtype: integer
		'''
		return self.size

def main():
	heap = BinaryMaxHeap(maxSize=7)
	print(heap.heap)
	heap.insert(1)
	print(heap.heap)
	heap.insert(2)
	print(heap.heap)
	heap.insert(3)
	print(heap.heap)
	heap.insert(7)
	print(heap.heap)
	heap.insert(5)
	print(heap.heap)
	heap.insert(6)
	print(heap.heap)
	heap.insert(7)
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
	heap.insert(1)
	print(heap.heap)
	heap.insert(2)
	print(heap.heap)
	heap.insert(3)
	print(heap.heap)
	heap.insert(7)
	print(heap.heap)
	heap.insert(5)
	print(heap.heap)
	heap.insert(6)
	print(heap.heap)
	heap.insert(7)
	print(heap.heap)

if __name__ == '__main__':
	main()
