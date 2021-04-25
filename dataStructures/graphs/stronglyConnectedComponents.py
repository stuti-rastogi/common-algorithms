from dataStructures.graphs.graphSearch import GraphSearch
from dataStructures.stacks import Stack

def findSCCs(g):
	# First DFS - store in stack by finishing times
	visited1 = set()
	stack = Stack(len(g.vertices))

	for v in g.vertices:
		if v not in visited1:
			dfsFinishingTimeOrder(g, v, visited1, stack)

	# Reverse the Graph
	g_reverse = reverseGraph(g)

	# DFS in decreasing order of finishing time
	visited2 = set()
	cnt = 1
	while not stack.isEmpty():
		s = stack.pop()
		if s not in visited2:
			print ("SCC {}: ".format(cnt), end="")
			g_reverse.dfsRecursiveHelper(s, visited2)
			print ()
			cnt += 1

def dfsFinishingTimeOrder(g, u, visited, stack):
	visited.add(u)
	for v in g.adj[u]:
		if v not in visited:
			dfsFinishingTimeOrder(g, v, visited, stack)
	stack.push(u)

def reverseGraph(g):
	g_reverse = GraphSearch()
	for v in g.vertices:
		g_reverse.addVertex(v)

	for u in g.adj:
		for v in g.adj[u]:
			g_reverse.addEdge((v, u))

	return g_reverse


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

	findSCCs(g)