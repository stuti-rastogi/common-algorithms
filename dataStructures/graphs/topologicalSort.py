import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
projectdir = os.path.dirname(parentdir)
sys.path.append(projectdir)

from dataStructures.graphs.graph import Graph
from dataStructures.queues import Queue

def topologicalSort_dfs(g):
    visited = set()
    # This is actually a stack, but since all we need is to push elements in order and then reverse,
    # a list also serves the purpose. Saves the trouble of implementing reverse method on the Stack class
    stack = []

    for v in g.vertices:
        if v not in visited:
            topologicalSort_dfsHelper(g, v, visited, stack)
    print ("Topological Sort by DFS: {}".format(stack[::-1]))

def topologicalSort_dfsHelper(g, u, visited, stack):
    visited.add(u)
    for v in g.adj[u]:
        if v not in visited:
            topologicalSort_dfsHelper(g, v, visited, stack)
    stack.append(u)


def topologicalSort_kahn(g):
    inDegree = [0] * len(g.vertices)
    visitedCnt = 0
    topologicalSort = []

    for u in g.adj:
        for v in g.adj[u]:
            inDegree[v] += 1

    q = Queue(len(g.vertices))

    for u in g.vertices:
        if inDegree[u] == 0:
            q.enqueue(u)

    while not q.isEmpty():
        u = q.dequeue()
        topologicalSort.append(u)
        visitedCnt += 1

        for v in g.adj[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                q.enqueue(v)

    if visitedCnt != len(g.vertices):
        raise Exception("Topological Sort not possible, cycle found")

    print ("Topological Sort by Indegree: {}".format(topologicalSort))


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge((5,0))
    g.addEdge((4,0))
    g.addEdge((4,1))
    g.addEdge((5,2))
    g.addEdge((2,3))
    g.addEdge((3,1))

    print ("\nGraph:\t", end="")
    g.print()
    topologicalSort_dfs(g)
    topologicalSort_kahn(g)

    # Test with a graph containing cycle

    g_cycle = Graph()
    for i in range(5):
        g_cycle.addVertex(i)

    g_cycle.addEdge((1,0))
    g_cycle.addEdge((2,1))
    g_cycle.addEdge((0,2))
    g_cycle.addEdge((0,3))
    g_cycle.addEdge((3,4))

    print ("\nGraph:\t", end="")
    g_cycle.print()
    # topologicalSort_dfs(g_cycle)          # this will work and print an ordering
    topologicalSort_kahn(g_cycle)
