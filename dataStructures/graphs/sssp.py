from weightedGraph import WeightedGraph
from dataStructures.minPriorityQueue import MinPriorityQueue


class SSSP(WeightedGraph):
	'''
		Class for single-source shortest paths solutions for weighted directed graphs
		1. Bellman-Ford - for graphs with negative weights
		2. Dijkstra - for graphs with non-negative weights
		3. ssspForDAG - for weighted directed acyclic graphs
	'''
	def __init__(self):
		self.distance = None
		self.parent = None
		super().__init__()


	def _initializeSSSP(self, s):
		lenV = len(self.vertices)
		self.distance = [float('inf')] * lenV
		self.distance[self.vertices[0]] = 0
		self.parent = [None] * lenV


	def _relax(self, u, v, w):
		if self.distance[v] > (self.distance[u] + w):
			self.distance[v] = self.distance[u] + w
			self.parent[v] = u


	def _printPaths(self, s):
		for v in self.vertices:
			if v == s:
				continue
			print ("Shortest path from {} to {} of weight {}\t: ".format(s, v, self.distance[v]), end="")
			currVertex = v
			stack = [currVertex]
			while currVertex:
				currVertex = self.parent[currVertex]
				stack.insert(0, currVertex)
			print (" -> ".join(map(str, stack)))


	def bellmanFord(self, s):
		'''
			Prints the shortest paths from s to every vertex v with the weight of the path
			If the graph has a negative-weighted cycle throws error
		'''
		self._initializeSSSP(s)

		for _ in range(len(self.vertices)-1):
			for edge in self.edges:
				self._relax(edge[0], edge[1], edge[2])

		for edge in self.edges:
			u, v, w = edge
			if self.distance[v] > (self.distance[u] + w):
				raise Exception("Negative-weight cycle found. SSSP not defined.")

		print ("\nOutput: ")
		self._printPaths(s)


	def dijkstra(self, s):
		'''
			Prints the shortest paths from s to every vertex v with the weight of the path
		'''
		self._initializeSSSP(s)
		queueArray = [(self.distance[i], i) for i in range(len(self.vertices))]
		q = MinPriorityQueue(queueArray)

		while not q.isEmpty():
			_, u = q.heapExtractMin()
			for (v, w) in self.adj[u]:
				if q.containsItem(v):
					self._relax(u, v, w)
					q.heapDecreaseKey(v, self.distance[v])

		print ("\nOutput: ")
		self._printPaths(s)


# testing code
if __name__ == "__main__":
	negativeWeightGraph  = SSSP()					# for Bellman-Ford
	positiveWeightGraph = SSSP()					# for Dijkstra
	dag = SSSP()

	for i in range(5):
		negativeWeightGraph.addVertex(i)
		positiveWeightGraph.addVertex(i)
		dag.addVertex(i)

	negativeWeightGraph.addDirectedEdge((0, 1, 6))
	negativeWeightGraph.addDirectedEdge((0, 3, 7))
	negativeWeightGraph.addDirectedEdge((4, 0, 8))
	negativeWeightGraph.addDirectedEdge((1, 2, 5))
	negativeWeightGraph.addDirectedEdge((4, 2, 7))
	negativeWeightGraph.addDirectedEdge((2, 1, -2))
	negativeWeightGraph.addDirectedEdge((3, 4, 9))
	negativeWeightGraph.addDirectedEdge((1, 3, 8))
	negativeWeightGraph.addDirectedEdge((3, 2, -3))
	negativeWeightGraph.addDirectedEdge((1, 4, -4))

	positiveWeightGraph.addDirectedEdge((0, 1, 10))
	positiveWeightGraph.addDirectedEdge((0, 3, 5))
	positiveWeightGraph.addDirectedEdge((4, 0, 7))
	positiveWeightGraph.addDirectedEdge((1, 2, 1))
	positiveWeightGraph.addDirectedEdge((2, 4, 4))
	positiveWeightGraph.addDirectedEdge((3, 1, 3))
	positiveWeightGraph.addDirectedEdge((3, 4, 2))
	positiveWeightGraph.addDirectedEdge((1, 3, 2))
	positiveWeightGraph.addDirectedEdge((3, 2, 9))
	positiveWeightGraph.addDirectedEdge((4, 2, 6))

	print ("\nBELLMAN FORD")
	print ("============")
	negativeWeightGraph.print()
	negativeWeightGraph.bellmanFord(0)
	print ("\n----------------------------------------------")

	print ("\nDIJKSTRA")
	print ("========")
	positiveWeightGraph.print()
	positiveWeightGraph.dijkstra(0)
	print ("\n----------------------------------------------")