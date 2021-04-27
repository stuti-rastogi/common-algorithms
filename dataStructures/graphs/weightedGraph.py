class WeightedGraph:
	'''
		Want to use weighted undirected graphs for MST and weighted directed graphs for SSSP
		Vertices stored in G.vertices, Vertices are just ints
		Edges stored in G.edges, in the form (u, v, w)
		Adjacency list stored in G.adj in the form: {u1: [(v1, w1), (v2, w2), ...], u2:[...], ...}
	'''

	def __init__(self):
		self.adj = {}
		self.vertices = []
		self.edges = []


	def addVertex(self, v):
		if v not in self.vertices:
			self.vertices.append(v)
			self.adj[v] = []
		else:
			print ("WARNING: Duplicate vertex added. Skipping...")


	def addUndirectedEdge(self, edge):
		'''
			Args:
				edge: tuple (u, v, w) - undirected edge between u and v vertices of weight w
			Function:
				Makes three updates:
					1. adds (u, v, w) to g.edges
					2. adds (v, w) to g.adj[u]
					3. adds (u, w) to g.adj[v]
		'''
		if type(edge) != tuple or len(edge) != 3:
			raise Exception("Badly formatted edge. Expected tuple of length 3.")

		if edge[0] not in self.vertices or edge[1] not in self.vertices:
			raise Exception("Edge between non-existing vertices. Please add vertex first.")

		self.edges.append(edge)
		self.adj[edge[0]].append(tuple(edge[1:]))
		self.adj[edge[1]].append(tuple([edge[0], edge[2]]))


	def addDirectedEdge(self, edge):
		'''
			Args:
				edge: tuple (u, v, w) - directed edge from u to v of weight w
			Function:
				Makes two updates:
					1. adds (u, v, w) to g.edges
					2. adds (v, w) to g.adj[u]
		'''
		if type(edge) != tuple or len(edge) != 3:
			raise Exception("Badly formatted edge. Expected tuple of length 3.")

		if edge[0] not in self.vertices or edge[1] not in self.vertices:
			raise Exception("Edge between non-existing vertices. Please add vertex first.")

		self.edges.append(edge)
		self.adj[edge[0]].append(tuple(edge[1:]))
