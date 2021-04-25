from dataStructures.queues import Queue
from dataStructures.stacks import Stack
from dataStructures.graphs.graph import Graph

class GraphSearch(Graph):
	'''
		Derived class of Graph class to define the search operations from Chapter 22, CLRS:
		1. BFS
		2. DFS
	'''
	def bfs(self, s):
		q = Queue(len(self.vertices))
		visited = set()

		q.enqueue(s)
		visited.add(s)
		print ("BFS: ", end="")

		while not q.isEmpty():
			u = q.dequeue()
			print (u, end=" ")
			for v in self.adj[u]:
				if v not in visited:
					visited.add(v)
					q.enqueue(v)
		print ()


	# Iterative DFS
	def dfsIterative(self, s):
		stack = Stack(len(self.vertices))
		visited = set()

		stack.push(s)
		visited.add(s)
		print ("Iterative DFS: ", end="")

		while not stack.isEmpty():
			u = stack.pop()
			print (u, end=" ")
			for v in self.adj[u]:
				if v not in visited:
					visited.add(v)
					stack.push(v)
		print()


	def dfsRecursive(self, s):
		visited = set()
		print ("Recursive DFS: ", end="")
		self.dfsRecursiveHelper(s, visited)
		print ()


	def dfsRecursiveHelper(self, u, visited):
		visited.add(u)
		print (u, end=" ")
		for v in self.adj[u]:
			if v not in visited:
				self.dfsRecursiveHelper(v, visited)


# testing code
if __name__ == "__main__":
	g = GraphSearch()
	for i in range(5):
		g.addVertex(i)

	g.addEdge((1,0))
	g.addEdge((2,1))
	g.addEdge((0,2))
	g.addEdge((0,3))
	g.addEdge((3,4))

	g.print()

	g.bfs(0)
	g.dfsIterative(0)
	g.dfsRecursive(0)