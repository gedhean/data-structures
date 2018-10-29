class Vertex:
	"""Graph vertex data structure"""
	def __init__(self, id):
		self.id = id
		self.connectedTo = {}
	
	def __str__(self):
		'Return the String representation of this Vertex'
		return str(self.id) + ' connected to ' + str([v.id for v in self.connectedTo])

	def addNeighbor(self, nbr, weight=0):
		'''
		Add a new Vertex to the list of neighbors of this vertex
		type nbr: integer or string
		type weight: number
		'''
		self.connectedTo[nbr] = weight

	def getId(self):
		'''
		Return the Vertex identifier
		rtype: integer or string
		'''
		return self.id

	def getNeighbors(self):
		'''
		Return a list of Vertex connected to this vertex
		rtype: dict_keys
		'''
		return self.connectedTo.keys()

	def getWeightOf(self, nbr):
		'''
		Return the weight of the given neighbor (nbr)
		type nbr: integer or str
		rtype: number
		'''
		return self.connectedTo[nbr]



class Graph:
	"""Graph data structure"""
	def __init__(self):
		'''
		Create a new empty directed weighted Graph
		'''
		self.vertices = {} 
		self.numVertices = 0
	
	def __contains__(self, vertex):
		return vertex in self.vertices

	def __iter__(self):
		return iter(self.list.values())

	def __str__(self):
		return 'Vertices: ' + str([v.id for v in self.vertices])

	def addVertice(self, key):
		'''
		Add a new Vertex to this graph
		'''
		self.numVertices += 1
		self.vertices[key] = Vertex(key)

	def getVertice(self, key):
		'''
		Return the Vertex object of the given key
		rtype: Vertex
		'''
		if key in vertices:
			return vertices[key]
		return None

	def addEdge(self, fromVertex, toVertex, weight=0):
		'''
		Add a new directed edge from fromVertex to toVertex vetices with the given wreight 
		'''
		if fromVertex not in self.vertices:
			self.addVertice(fromVertex)
		if toVertex not in self.vertices:
			self.addVertice(toVertex)
		self.vertices[fromVertex].addNeighbor(toVertex, weight)
