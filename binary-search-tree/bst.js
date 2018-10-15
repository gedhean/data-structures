/*
 Binary-Search Tree implementation in JavaScript <3
*/

class Node {
	constructor(value) {
		this.value = value
		this.left = null
		this.right = null
	}
}

class BinarySearchTree {
	constructor() {
		this.root = null
	}
	/*
		Insert the given value in that BST and keeps it ordered
	*/
	insert(value) {
		const newNode = new Node(value)
		if (this.root == null) {
			this.root = newNode
		} else {
			let current = this.root
			while (!!current) {
				if (value < current.value) {
					if (!current.left) {
						current.left = newNode
						break
					}
					current = current.left
				}
				else if (value > current.value) {
					if (!current.right) {
						current.right = newNode
						break
					}
					current = current.right
				} else {
					break
				}
			}
    }
    return this
	}
	/*
		Return true if that BST contains the given value or false otherwise
	*/
	contains(value) {
		let current = this.root
		while(!!current) {
			if (current.value == value) return true
			else if (value < current.value) {
				current = current.left
			} 
			else {
				current = current.right
			}
		}
		return false
	}
	/*
		Return the max value in that BST
	*/
	getMax(node) {
		if (!node) node = this.root
		while (node.right) {
			node = node.right
		}
		return node ? node.value : null	
	}
	/*
		Return the min value in that BST
	*/
	getMin(node) {
		if (!node) node = this.root
		while (node.left) {
			node = node.left
		}
		return node ? node.value : null	
	}
	/*
		Delete the given value from that BST
		@param value {number}- The value to be deleted
		@retrun this {BinarySearchTree}
	*/
	delete(value) {
		this.root = this._removeNode(this.root, value)
		return this
	}
	/*
		Traverse that BST visiting every node in each level and applay the fn function
		in nodes
		@param fn {function} Function to be applied in the nodes
		@retrun void
	*/
	traverseBreadthFirst(fn) {
		let queue = [], node = null
		// Must use a better queue implementation 
		// with queue and dequeue O(1)
		queue.push(this.root)
		while (queue.length) {
			node = queue.shift()
			fn(node)
			node.left && queue.push(node.left) 
			node.right && queue.push(node.right) 
		}
	}
	/*
		Helper function to delete the given value in the node Tree
		@param node {Node} The binary where the value should be removed
		@param value {number} The node value to be removed from the node BST
		@retrun {Node} The BST with the given value deleted
	*/
	_removeNode(node, value) {
		// Base case
		if (!node) return null
		// Find node to be deleted
		if (node.value == value){
			// Is leaf: Just delete it!
		  if (this._isLeaf(node)) return null
			// Has only right child: point to it
			else if (!node.left) return node.right
			// Has only left child: point to it
			else if (!node.right) return node.left
			// Has two children
			// Try to reassign with the left child successor
			// To keep the BST property 
			else {
				let successor = this.getMin(node.right)
				node.value = successor
				// remove a leaf
				node.right = this._removeNode(node.right, successor)	
			}
		}
		// Look for the node to be deleted in the left sub tree  
		else if (value < node.value) {
			node.left = this._removeNode(node.left, value)
			return node		
		} 
		// Look for the node to be deleted in the righ sub tree  
		else if (value > node.value){
			node.right = this._removeNode(node.right, value)
			return node
		}
		return node
	}
	/*
		Check if the given node is a leaf or not
		@param node {Node} The node to be checked
		@return bool 
	*/
	_isLeaf(node) {
		if (node && !node.left && !node.right) return true
		else return false
	}
}

const bst = new BinarySearchTree()
console.log(bst)
bst.insert(10).insert(5).insert(15).insert(1).insert(6).insert(12).insert(20).insert(2)
console.log(bst)
console.log('BST contains 10?', bst.contains(10))
console.log('BST contains 1?', bst.contains(1))
console.log('BST min value:', bst.getMin())
console.log('BST max value:', bst.getMax())
bst.delete(1)
console.log('BST contains 1?', bst.contains(1))
console.log(bst)
bst.delete(10)
console.log('BST contains 10?', bst.contains(10))
console.log(bst)