class TreeNode:
	"""
	docstring for TreeNode
	Representation of Node in a binary tree
	"""
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
		return self.right

# Depth-First-Search (DFS) - Pre Order traverse
# 1. visit root
# 2. go left
# 3. go right
def preorderTraversalRec(root):
	"""
	Recursive version of DFS - preorder traverse
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is not None:
		return [root.value] + preorderTraversalRec(root.left) + preorderTraversalRec(root.right)
	else:
		return []

def preorderTraversalIt(root):
	"""
	Iterative version of DFS - preorder traverse
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

# Depth-First-Search (DFS) - In Order traverse
# 1. go left
# 2. visit root
# 3. go right
def inorderTraversalRec(root):
	"""
	Recursive version of DFS - In order traverse
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is not None:
		return inorderTraversalRec(root.left) + [root.value] + inorderTraversalRec(root.right)
	else:
		return []

def inorderTraversalIt(root):
	"""
	Iterative version of DFS - In order traverse
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is None: 
		return []

	# code goes here
	stack = []
	currentNode = root
	result = []
	while 1:
		# Go to the left most node leaf
		if currentNode.left is not None:
			stack.append(currentNode)
			currentNode = currentNode.left
		# Otherwise, try to do that starting from the right child
		else:
			result.append(currentNode.value)	
			if currentNode.right is not None:
				currentNode = currentNode.right
			else:
				if len(stack) is 0:
					break
				currentNode = stack.pop()
				result.append(currentNode.value)
				if currentNode.right is not None:
					currentNode = currentNode.right
				else: 
					break

	return result
# Depth-First-Search (DFS) - Post Order traverse
# 1. go left
# 2. go right
# 3. visit root
def postorderTraverseRec(root):
	"""
	Recursive version of DFS - In order traverse
    :type root: TreeNode
    :rtype: List[int]
    """
	if root is None:
		return []
	return postorderTraverseRec(root.left) + postorderTraverseRec(root.right) + [root.value]

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

	print("Test 1 <======== Pre order - Recursive =========>")
	print("Output: ", preorderTraversalRec(T1))
	print("Answer: ", "[1, 2, 4, 5, 3, 7]")
	# base case
	print("Test 2 <========= Pre order - Iterative ========>")
	print("Output: ", preorderTraversalIt(T1))
	print("Answer: ", "[1, 2, 4, 5, 3, 7]")

	print("Test 3 <========= In order - Recursive ========>")
	print("Output: ", inorderTraversalRec(T1))
	print("Answer: ", "[4, 2, 5, 1, 7, 3]")

	print("Test 4 <========= In order - Iterative ========>")
	print("Output: ", inorderTraversalIt(T1))
	print("Answer: ", "[4, 2, 5, 1, 7, 3]")

	print("Test 5 <========= Post order - Recursive ========>")
	print("Output: ", postorderTraverseRec(T1))
	print("Answer: ", "[4, 5, 2, 7, 3, 1]")

if __name__ == '__main__':
	main()