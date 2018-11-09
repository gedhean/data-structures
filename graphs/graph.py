class Vertex:
	"""Graph vertex data structure"""
	def __init__(self, id):
		'''
		Create a new graph vertex.
		type id: integer or string - unique vertex identifier
		'''
		self.id = id 			
		# Dictinary of vertices connected with that vertex. { key-vertex id: value-weight }
		# A vertex V is `connected to` that vertex if there is an edge from that vertex to V
		self.connectedTo = {}	
	
	def __str__(self):
		'Return the String representation of this Vertex'
		return str(self.id) + ' connected to ' + str([v for v in self.connectedTo])

	def addNeighbor(self, nbr, weight=0):
		'''
		Add a new Vertex to the list of neighbors of this vertex
		type nbr: integer or string - vertex id
		type weight: number			- edge weight
		'''
		self.connectedTo[nbr] = weight

	def getId(self):
		'''
		Return the Vertex identifier
		rtype: integer or string - vertex id
		'''
		return self.id

	def getNeighbors(self):
		'''
		Return a list of vertices (id) connected to that vertex
		rtype: dict_keys - vetices id
		'''
		return self.connectedTo.keys()

	def getWeightOf(self, nbr):
		'''
		Return the weight of the given neighbor (nbr)
		type nbr: integer or str - vertex id
		rtype: number 			 - edge weight
		'''
		return self.connectedTo[nbr]

class Graph:
	"""Weight Directed Graph (WDG)data structure"""
	def __init__(self):
		'''
		Create a new empty DWG
		'''
		self.vertices = {} 
		self.numVertices = 0
	
	def __contains__(self, vertex):
		return vertex in self.vertices

	def __iter__(self):
		return iter(self.list.values())

	def __str__(self):
		return 'Vertices: ' + str([v for v in self.vertices])

	def addVertice(self, key):
		'''
		Add a new Vertex to that Graph
		type key: integer or string - vertex id
		'''
		self.numVertices += 1
		self.vertices[key] = Vertex(key)

	def getVertice(self, key):
		'''
		Return the Vertex object of the given key
		rtype: integer or string - vertex id 
		'''
		if key in self.vertices:
			return self.vertices[key]
		return None

	def addEdge(self, fromVertex, toVertex, weight=0):
		'''
		Add a new directed edge from fromVertex to toVertex vetices with the given weight
		type fromVertex: integer or string - vertex id 
		type toVertex: 	 integer or string - vertex id 
		type weight:	 integer 		   - edge weight
		'''
		if fromVertex not in self.vertices:
			self.addVertice(fromVertex)
		if toVertex not in self.vertices:
			self.addVertice(toVertex)
		self.vertices[fromVertex].addNeighbor(toVertex, weight)

from queue import Queue

def bfs(graph, start_vertex):
	'''Breadth-First Search graph algorithm'''
	parent  = {}					# Vertex parent, also keep the visited vertices 
	discovered = Queue()			# Discovered vertices
	discovered.put(start_vertex)	# Enqueue start vertex
	parent[start_vertex] = None		# Start vertex do not have parent
	
	while not discovered.empty():		# Loop throghout all vertices
		current = discovered.get()  	# Dequeue vertex
		for nbr in graph.getVertice(current).getNeighbors():
			if nbr not in parent:
				discovered.put(nbr)		# Enqueue discovered vertices
				parent[nbr] = current	# Store vertex parent	
	return parent	

if __name__ == '__main__':
	g = Graph()
	g.addEdge(1,2)
	g.addEdge(1,3)
	g.addEdge(1,4)
	g.addEdge(2,1)
	g.addEdge(3,1)
	g.addEdge(4,1)
	g.addEdge(3,4)
	g.addEdge(4,3)
	g.addEdge(3,5)
	g.addEdge(5,3)
	g.addEdge(5,6)
	g.addVertice(7)
	print('graph: ', g)

	print('BFS 1: ', bfs(g, 1))
	print('BFS 5: ', bfs(g, 5))
	print('BFS 7 disconexed: ', bfs(g, 7))

