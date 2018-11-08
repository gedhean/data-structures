INITIAL_SIZE = 10								# Intial array size

class Queue:
	"""FIFO Queue Data Structure implementation with array"""
	def __init__(self):
		'''Create a new empty queue'''
		self._queue 	= [None] * INITIAL_SIZE	# Array to store queue elements
		self._size 		= 0						# Number of elements in queue
		self._capacity 	= INITIAL_SIZE			# Max number of elements 
		self._start 	=  0					# Index to point to FIRST element in queue
		self._end 		= -1					# Index to point to LAST element in queue
	
	def enqueue(self, element):
		'''Insert the given elemetn at the and of queue'''
		if self.isFull():
			self._resize()
		self._size += 1 
		self._end = self._nextIndex(self._end)
		self._queue[self._end] = element

	def dequeue(self):
		'''
		Remove the first element in queue
		
		Raise a Empty error if queue is empty
		'''
		if self.isEmpty():
			raise Exception('Queue is empty')
		
		self._size -= 1 							# Decrase queue size
		value = self._queue[self._start]			# Store value to be dequeued
		self._queue[self._start] = None 			# Erase dequeued element
		self._start = self._nextIndex(self._start)	# Update first queue element
		return value

	def size(self):
		'''Return number of elements in queue'''
		return self._size

	def isEmpty(self):
		'''Return true if queue is empty'''
		return self._size == 0

	def isFull(self):
		'''Return true if queue is full'''
		return self._size == self._capacity


	def _nextIndex(self, index):
		'''Calcule the in an cirular array'''
		return (index + 1) % self._capacity

	def _resize(self):
		'''Double the queue capacity'''
		oldQueue = 			self._queue					# Save old queue values to copy later
		oldStart = 			self._start 					
		oldCapacity = 		self._capacity
		self._capacity = 	2 * oldCapacity 			# Double queue capacity 	
		self._queue = 		[None] * self._capacity		# Create new queue with new capacity
	    
		for newStart in range(oldCapacity):				# Copy all elements in old queue to new queue
			self._queue[newStart] = oldQueue[oldStart]	# Shift elements in old queue to begin of new queue
			oldStart = (oldStart + 1) % oldCapacity		# Calcule next index in circular array
	    
		self._start = 0									# Update new start index (first element in queue)
		self._end = oldCapacity - 1						# Update new end index (last element in queue)
	
	def __str__(self):
		return str(self._queue)

if __name__ == '__main__':
	q = Queue()
	print('Size:', q.size())
	for x in range(5):
		q.enqueue(x)
	print('Enqueue 0 to 4 elements:', q)
	print('Size:', q.size())

	for x in range(3):
		q.dequeue()
	print('Dequeue 3 elements:', q)
	print('Size:', q.size())

	for x in range(15):
		q.enqueue(x)
	print('Enqueue 0 to 14 elements:', q)
	print('Size:', q.size())

	for x in range(10):
		q.dequeue()
	print('Dequeue 10 elements:', q)
	print('Size:', q.size())

	for x in range(31):
		q.enqueue(x)
	print('Enqueue 0 to 30 elements:', q)
	print('Size:', q.size())

	for x in range(38):
		q.dequeue()
	print('Dequeue 38 elements:', q)
	print('Size:', q.size())
