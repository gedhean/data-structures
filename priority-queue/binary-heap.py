from math import floor

class BinaryMaxHeap:
	"""Represent a Binary Max Heap"""
	def __init__(self, maxSize):
		self.heap = [None] * maxSize
		self.size = 0 
		self.maxSize = maxSize
	
	def getValue(self, index):
		if self.size != 0 and index <= self.size:
			return self.heap[index - 1]

	def setValue(self, index, value):
		if index > self.size and index < 1:
			print('Could not set value. Invalid index.')
			return
		self.heap[index - 1] = value

	def insert(self, value):
		'''
		Insert the given value in the BinaryMaxHeap
		type value: integer
		rtype: void
		'''
		# heap is full
		if self.size >= self.maxSize:
			print('Could not insert. Heap if full!')
			return

		lastIndex = self.size if self.size != 0 else 1
		parentIndex = self.getParentIndex(lastIndex)
		index = self.getLeftChildIndex(parentIndex) if (lastIndex % 2 == 1) else self.getRightChildIndex(parentIndex)
		self.setValue(index, value)
		self.size += 1
		self.siftUp(index)

	def extractMax(self):
		if self.size == 0:
			print('Could not extractMax. Heap is empty!')
			return None
		
		lastValueIndex = self.size
		maxValue = self.getValue(1)
		self.swapValues(1, lastValueIndex)
		self.getValue(lastValueIndex, None)
		self.size -= 1
		self.siftDown(1)
		return maxValue

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
		childIndex = leftChildIndex if self.getValue(leftChildIndex) > self.getValue(rightChildIndex) else rightChildIndex

		while (self.getValue(parentIndex) < self.getValue(childIndex)) and (childIndex < self.size):
			
			self.swapValues(parentIndex, childIndex)
			parentIndex = childIndex
			rightChildIndex = self.getRightChildIndex(parentIndex)
			leftChildIndex = self.getLeftChildIndex(parentIndex)
			childIndex = leftChildIndex if self.getValue(leftChildIndex) > self.getValue(rightChildIndex) else rightChildIndex
	
	def getParentIndex(self, index):
		'''
		Retrun the parent index of the given elment index.
		type index: integer
		rtype: integer
		'''
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

	def swapValues(self, index1,index2):
		'''
		Swap two values in the BinaryMaxHeap
		type index1: integer
		type index2: integer
		rtype; void
		'''
		temp = self.getValue(index1)
		self.setValue(index1, self.getValue(index2)) 
		self.setValue(index2, temp)

def main():
	heap = BinaryMaxHeap(maxSize=7)
	print(heap.heap)
	heap.insert(2)
	heap.insert(3)
	heap.insert(4)
	heap.insert(-1)
	heap.insert(5)
	heap.insert(5)
	heap.insert(0)
	print(heap.heap)
	print('extractMax: ', heap.extractMax())
	print(heap.heap)
if __name__ == '__main__':
	main()
