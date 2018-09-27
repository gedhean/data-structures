class TreeNode:
	"""docstring for TreeNode"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def addLeft(self, value):
		"""
		Add a TreeNode with the given value at left 
		:type value: integer or any
		:rtype: TreeNode
		"""
		self.left = TreeNode(value)
		return self.left 

	def addRight(self, value):
		"""
		Add a TreeNode with the given value at right 
		:type value: integer or any
		:rtype: TreeNode
		"""
		self.right = TreeNode(value)
		return self

# Depth-First-Search (DFS) - Pre Order
# 1. visit root
# 2. go left
# 3. go right
def preorderTraversalRec(root):
	"""
	Recursive version of DFS - preorder
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is not None:
		return [root.value] + preorderTraversalRec(root.left) + preorderTraversalRec(root.right)
	else:
		return []

def preorderTraversalIt(root):
	"""
	Iterative version of DFS - preorder
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is None: 
		return []

	result = []
	stack = [root]
	
	while len(stack) is not 0:
		currentNode = stack.pop()
		result.append(currentNode.value)

		if currentNode.right is not None:
			stack.append(currentNode.right)
		if currentNode.left is not None:
			stack.append(currentNode.left)
	
	return result

def main():
	"""
			1
		  /	  \
	    2 		3
	   / \     / 
     4	  5	  7
	"""
	T1 = TreeNode(1)
	T1.addLeft(2)
	T1.addRight(3)
	T1.left.addLeft(4)
	T1.left.addRight(5)
	T1.right.addLeft(7)

	print("Test 1 <=================>")
	print("Output: ", preorderTraversalRec(T1))
	print("Answer: ", "[1, 2, 4, 5, 3, 7]")
	# base case
	print("Test 2 <=================>")
	print("Output: ", preorderTraversalRec(None))
	print("Answer: ", "[]")

if __name__ == '__main__':
	main()