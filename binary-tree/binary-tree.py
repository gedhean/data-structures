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

def postorderTraverseIt(root):
	"""
	Iteractive version of DFS - In order traverse
    :type root: TreeNode
    :rtype: List[int]
    """
	result = []

	if root is None:
		return result

	stack = [root]
	# Perform a preorder
	while stack:
		current = stack.pop()
		result.append(current.value)
		if current.left:
			stack.append(current.left)
		if current.right:
			stack.append(current.right)
	result.reverse()
	return result
# Breadth-First Search
def bfs(root):
	"""
	Iteractive version of BFS - Binary Tree traverse
    :type root: TreeNode
    :rtype: List[List[int]]
    """
	if root is None:
		return []
	queue = [[root]]
	result = []
	for level in queue:
		nextLevel = []
		levelRes = []
		for node in level:
			levelRes.append(node.value)
			if node.left:
				nextLevel.append(node.left)
			if node.right:
				nextLevel.append(node.right)
		result.append(levelRes)
		if nextLevel:
			queue.append(nextLevel)
	return result

def isSymmetric(root):
	'''
	Return true if the given tree is symmetric with relation to root or false otherwise.
	type root: TreeNode
	rtype: bool
	'''
	if root:
		return isMirrorTree(root.left, root.right)
	return True

def isMirrorTree(T1,T2):
	'''
	Return true if the given trees are mirror of each other or false otherwise.
	type T1: TreeNode
	type T2: TreeNode
	rtype: bool
	'''
	if T1 is None and T2 is None:
		return True
	elif T1 is None or T2 is None:
		return False
	else:
		if T1.value == T2.value:
			leftSubTree = isMirrorTree(T1.left, T2.right)
			rightSubTree = isMirrorTree(T1.right, T2.left)
			return leftSubTree and rightSubTree
		else:
			return False

def isLeaf(node):
	'''
	Return true if the given node if a leaf or false otherwise.
	type node: TreeNode
	rtype: bool 
	'''
	if node and node.left is None and node.right is None:
		return True
	else:
		return False

def hasPathSum(root, sum):
	'''
	Given the number sum and a binary tree (root), return true if exist a root-to-leaf path in the tree that the sum
	of the node values in the path is equals to sum param. Otherwise, return false.
	type root: TreeNode
	rtype: bool
	'''
	if not root:
		return False
	else:
		if not root.left and not root.right and root.value == sum:
			return True
		else:
			newSum = sum - root.value
			return hasPathSum(root.left, newSum) or hasPathSum(root.right, newSum)

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

	print("Test 6 <========= Post order - Iterative ========>")
	print("Output: ", postorderTraverseIt(T1))
	print("Answer: ", "[4, 5, 2, 7, 3, 1]")


	print("Test 7 <======== Breadth-First Search ===========>")
	print("Output: ", bfs(T1))
	print("Answer: ", "[[1], [2, 3], [4, 5, 7]]")

	T2 = TreeNode(2)
	T2.addLeft(1).addRight(3)
	T2.addRight(3).addLeft(1)
	print("Test 8 <======== Check for isSymmetric ===========>")
	print("Output: ", isSymmetric(T2))	

if __name__ == '__main__':
	main()