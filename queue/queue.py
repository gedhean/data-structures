class Queue:
	"""FIFO Queue Data Structure implementation with Linked List"""
	def __init__(self):
		'''Create a new empty queue'''
		self._size = 0
		self._start = None
		self._end = None

	def enqueue(self, element):
		
		