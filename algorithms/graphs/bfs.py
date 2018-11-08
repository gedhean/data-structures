from queue import Queue

def bfs(graph, start_vertex):
	'''Breadth-First Search graph algorithm'''
	parent  = {}					# Vertex parent 
	visited = {}					# Visited vertices (helpful to avoid infinity loops)
	discovered = Queue()			# Discovered vertices
	step = 1
	discovered.put(start_vertex)	# Enqueue start vertex
	visite[start_vertex] = 0
	parent[start_vertex] = None
	
	while not discovered.empty():
		current = discovered.get()  # Dequeue vertex
		for nbr in graph.getVertice(current).getNeighbors():
			if nbr not in visited:
				discovered.put(nbr)		# Enqueue discovered vertices
				parent[nbr] = current
				visited[nbr] = step
		step += 1
