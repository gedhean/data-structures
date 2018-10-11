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
	Return a new BST sroted with the given value inserted
	type root: TreeNode
	type value: integer or any
	rtype: TreeNode
	'''
	if root is None:
		# Arguments are passed by objetc reference
		# root is a local variable
		root = TreeNode(value)
	elif value < root.value:
		root.left = insert(root.left, value)
	elif value > root.value:
		root.right = insert(root.right, value)
	return root
	# Does not insert duplicated values

def find(root, value):
	'''
	Retrun true if value is in the BST or false otherwise.
	type root: TreeNode
	type value: integer
	rtype: boolean
	'''
	if root is None:
		return False
	if root.value == value:
		return True
	elif value < root.value:
		return find(root.left, value)
	elif value > root.value:
		return find(root.right, value)

def count_nodes(root):
	'''
	Return the number of elements in the BST
	tpye root: TreeNode
	rtype: integer
	'''
	if root is None:
		return 0
	else:
		return 1 + count_nodes(root.left) + count_nodes(root.right)

def print_values(root):
	'''
	Print all values in an BST asc (in order traverse)
	'''
	if root:
		print_values(root.left)
		print(root.value, end=" ")
		print_values(root.right)

def delete_tree(root):
	'''
	Delete_tree a BST
	rtype: void
	'''
	if root:
		delete_tree(root.left)
		delete_tree(root.right)
		del root

def height(root):
	'''
	Return the height of the BST
	rtype: integer
	'''
	if root is None:
		return 0
	return 1 + max(height(root.left), height(root.right))

def get_min(root):
	'''
	Return the min value in the BST.
	rtype: interge or None
	'''
	if root:
		if root.left:
			return get_min(root.left)
		return root.value
	return None

def get_max(root):
	'''
	Return the max value in the BST.
	rtype: interge or None
	'''
	if root:
		if root.right:
			return get_max(root.right)
		return root.value
	return None

def delete(root, value):
	'''
	Delete the given value in the BST and return a new BST without that value
	type root: TreeNode
	type value: integer
	rtype: TreeNode
	'''
	if root.value == value:
		if root.left:
			root.value = get_max(root.left)
			root.left = delete(root.left, root.value)
		elif root.right:
			root.value = get_min(root.right)
			root.right = delete(root.right, root.value)
		else:
			root = None
	elif value < root.value:
		root.left = delete(root.left, value)
	else:
		root.right = delete(root.right, value)
	return root


def print_breadth(root):
	if not root:
		return
	levels = [[root]]

	for nodes in levels:
		nextLevel = []
		for node in nodes:
			print(node.value, end=" ")
			if node.left:
				nextLevel.append(node.left)
			if node.right:
				nextLevel.append(node.right)
		print('')
		if nextLevel:
			levels.append(nextLevel)


def main():
	T1 = TreeNode(5)
	T2 = insert(T1, 6)
	T3 = insert(T2, 3)
	print('BST values in order:')
	print_values(T3)
	print('\n\nBreadth-First Search in BST values T3:')
	print_breadth(T3)
	print('\n\n<================================>')
	print('Is number 3 in the BST T3?', find(T3, 3))
	print('\n<================================>')
	print('Is number 10 in the BST T3?', find(T3, 10))
	print('\nNumber of nodes in hte BST T3:', count_nodes(T3))
	print('\nTree height T3: ', height(T3))
	T4 = insert(T3, -1)
	print('\n\nBreadth-First Search in BST values T4:')
	print_breadth(T4)
	print('\nTree height T4: ', height(T4))
	print('\nGet min value T4: ', get_min(T4))
	print('\nGet max value T4: ', get_max(T4))
	T5 = delete(T4, 6)
	print('\n\nBreadth-First Search in BST values T4 after delete node 6:')
	print_breadth(T5)

	#delete_tree(T3)
	#print('\nDelete the BST ->', T3.value)

if __name__ == '__main__':
	main()
