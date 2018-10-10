class TreeNode:
	"""
	Represent a binary tree node
	:type value: integer or any
	:type left: TreeNode or None
	:type right: TreeNode or None
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
def insert(root, value):
	'''
	Return a new BST with the given value inserted	
	type root: TreeNode
	type value: integer or any
	rtype: TreeNode
	'''
	if root is None:
		# Arguments are passed by values
		root = TreeNode(value)
	elif value < root.value:
		root.left = insert(root.left, value)
	elif value > root.value:
		root.right = insert(root.right, value)
	return root
	# Does not insert duplicated values

def print_values(root):
	'''
	Print all values in an BST (in order traverse)
	'''
	if root:
		print_values(root.left)
		print(root.value)
		print_values(root.right)

def main():
	T1 = TreeNode(5)
	T2 = insert(T1, 6)
	T3 = insert(T2, 8)
	print_values(T3)

if __name__ == '__main__':
	main()
