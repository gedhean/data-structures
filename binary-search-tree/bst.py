class BST:
	"""
	Binary Search Tree
	Properteis left and right are a reference to another Node	
	"""
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		'''
		Add a Node with the given value in the BST
		:type value: integer or any
		:rtype: void
		'''
		# Root
		if self.value is None:
			self.value = value
		elif value < self.value:
			if self.left:
			 	self.left.insert(value)
			else:
				self.left = BST(value)
		elif value > self.value:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BST(value)
		# Do not insert duplicated values

	def get_node_count(self):
		'''
		Return the number of nodes in the BST
		rtype: integer
		'''
		return 0

	def print_values(self):
		'''
		Print all values in BST from min to max value
		rtype: void
		'''
		if self.left:
			self.left.print_values()
		print(self.value, end=', ')
		if self.right:
			self.right.print_values()
def main():
	bst = BST()
	bst.insert(5)
	bst.insert(4)
	bst.insert(6)
	bst.insert(3)
	bst.insert(3)
	bst.insert(1000)
	bst.insert(8)

	bst.print_values()
	count_nodes = bst.get_node_count()
	print('Count nodes:', count_nodes)
	# print(bst.root)

if __name__ == '__main__':
	main()