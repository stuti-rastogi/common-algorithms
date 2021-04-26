class WeightedGraph:
	'''
		Redefining graph class, not using dataStructures.graphs.Graph
		Want to use weighted undirected graphs for MST
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


	def addEdge(self, edge):
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


	def kruskalMST(self):
		'''
			Kruskal's Algorithm to find the MST
			Prints the MST array containing edges of an MST
		'''
		def findRoot(parent, v):
			'''
				Find operation of union-find with path compression
				Returns root of current node and updates parent of all nodes in path to the root
			'''
			if parent[v] != v:
				parent[v] = findRoot(parent, parent[v])
			return parent[v]

		def union(parent, rank, x, y):
			xRoot = findRoot(parent, x)
			yRoot = findRoot(parent, y)
			if rank[xRoot] < rank[yRoot]:
				parent[xRoot] = yRoot
			elif rank[xRoot] > yRoot:
				parent[yRoot] = xRoot
			else:
				parent[yRoot] = xRoot
				rank[xRoot] += 1

		MST = []

		# sort edges in non-decreasing order by weight
		sortedEdges = sorted(self.edges, key=lambda item: item[2])

		# arrays for union-find
		lenV = len(self.vertices)
		parent = [v for v in self.vertices]
		rank = [0] * lenV

		mstSize = 0							# iterator for the edges added to MST
		edge = 0							# iterator for the edges in sortedEdges
		while mstSize < (lenV-1):
			(u, v, w) = sortedEdges[edge]
			x = findRoot(parent, u)
			y = findRoot(parent, v)

			# if u and v belong to different subsets, add to MST by taking union
			if x != y:
				mstSize += 1
				MST.append(sortedEdges[edge])
				union(parent, rank, x, y)
			
			edge += 1

		# printing the MST
		print ("\nKruskal MST:")
		mstWeight = 0
		for edge in MST:
			u, v, w = edge
			print ("{} --- {} : {}".format(u, v, w))
			mstWeight += w
		print ("MST Weight: {}".format(mstWeight))


	def primMST(self):
		'''
			Prim's Algorithm to find the MST
			Prints the MST array containing edges of an MST
		'''
		from dataStructures.minPriorityQueue import MinPriorityQueue
		pass

		# lenV = len(self.vertices)
		# # initialize keys of all vertices and take vertex 0 as root
		# key = [float('inf')] * lenV
		# key[self.vertices[0]] = 0

		# parent = [-1] * lenV
		# q = MinPriorityQueue(key)
		# q.printHeap()

		# while not q.isEmpty():
		# 	u = q.heapExtractMin()
		# 	for edge in g.adj[u]:
		# 		v, w = edge
		# 		if v in q.heap and w < q.heap[v]:
		# 			parent[v] = u
		# 			q.heapDecreaseKey(v, w)


		# # printing the MST
		# print ("\Prim MST:")
		# for i in range(1, lenV):
		# 	print ("{} --- {}".format(parent[i], i))


	def print(self):
		print ("\nGraph:")
		for u in self.adj:
			print ("{} : {}".format(u, self.adj[u]))


# testing code
if __name__ == "__main__":
	g = WeightedGraph()
	for i in range(9):
		g.addVertex(i)

	g.addEdge((0, 1, 4))
	g.addEdge((1, 2, 8))
	g.addEdge((2, 3, 7))
	g.addEdge((3, 4, 9))
	g.addEdge((4, 5, 10))
	g.addEdge((5, 6, 2))
	g.addEdge((6, 7, 1))
	g.addEdge((7, 0, 8))
	g.addEdge((1, 7, 11))
	g.addEdge((2, 8, 2))
	g.addEdge((8, 7, 7))
	g.addEdge((8, 6, 6))
	g.addEdge((2, 5, 4))
	g.addEdge((3, 5, 14))

	g.print()
	g.kruskalMST()
	g.primMST()
