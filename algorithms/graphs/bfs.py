from queue import Queue

def bfs(graph, start_vertex):		# Use Graph DS in graphs/graph.py
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
