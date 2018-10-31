class ListNode:
	"""Linked List node"""
	def __init__(self, value):
		'''Creata a new ListNode with the given value'''
		self._value = value
		self._next = None

	def __str__(self):
		return str(self._value) + "->" + str(self._next)

	def getValue(self):
		'''Retrurn the node value'''
		return self._value

	def setNext(self, listNode):
		'''Set next ListNode'''
		self._next = listNode

	def getNext(self):
		'''Return next ListNode'''
		return self._next

class LinkedList:
	"""Linked List Data Structure"""
	def __init__(self):
		'''Create a new empty Linked List'''
		self._head = None
		self._tail = None
		self._size = 0

	def __str__(self):
		return str(self._head) 
		
	def isEmpty(self):
		'''Return true if the Linked List is empty'''
		return self._size == 0
	def size(self):
		'''Return the number of elements'''
		return self._size

	def pushBack(self, value):
		'''Add a element at the end'''
		newNode = ListNode(value)
		if self.isEmpty():
			self._head = newNode
			self._tail = self._head
		else:
			self._tail.setNext(newNode)
			self._tail = self._tail.getNext()
		self._size += 1

	def popFront(self):
		'''
		Return and remove the first element

		Raise an Empty error if is empty
		'''
		if self.isEmpty():
			raise Empty('Linked List is empty')
		else:
			value = self._head.getValue()
			if self.size() == 1:
				self._head = None
				self._tail = None
			else:
				self._head = self._head.getNext() 
			self._size -= 1
		return value



		
		