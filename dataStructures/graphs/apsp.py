# Solutions to all pairs shortest paths problems
# 1. Basic DP Solution
# 2. Floyd-Warshall
# 3. Johnson

from denseWeightedGraph import DenseWeightedGraph, printMatrix
from weightedGraph import WeightedGraph
from sssp import SSSP

def fastDPAlgo(g):
    '''
        g is a weighted directed graph represented by an adjacency matrix - DenseWeightedGraph type
        O(V^3*lgV) solution
    '''
    distance = g.adj
    m = 1
    while m < (g.v - 1):
        distanceUpdate = [[float('inf') for i in range(g.v)] for i in range(g.v)]
        for i in range(g.v):
            for j in range(g.v):
                for k in range(g.v):
                    distanceUpdate[i][j] = min(distanceUpdate[i][j], distance[i][k] + distance[k][j])
        distance = distanceUpdate
        m = 2 * m
    return distance


def floydWarshall(g):
    '''
        g is a weighted directed graph represented by an adjacency matrix - DenseWeightedGraph type
        O(V^3) solution
    '''
    distance = g.adj
    for k in range(g.v):
        for i in range(g.v):
            for j in range(g.v):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    return distance


def johnson(g):
    '''
        g is a weighted directed graph represented by an adjacency list - WeightedGraph
        (For Johnson's we use an adjacency list)
        O(VE + VElgV) solution
    '''
    # Add dummy source vertex and edges
    lenV = len(g.vertices)
    # Since we assume vertices are 0 to |V|-1, our new vertex has id |V|
    s = lenV
    g.addVertex(s)
    for i in range(lenV):
        g.addDirectedEdge((s, i, 0))

    # Run Bellman-Ford to get vertex weight function
    h = g.bellmanFord(s)

    # Remove the dummy vertex
    g.removeVertex(s)

    # reweighting
    for u in g.adj:
        g.adj[u][:] = [(v, w+h[u]-h[v]) for (v,w) in g.adj[u]]

    distance = [[float('inf') for i in range(lenV)] for i in range(lenV)]
    for u in g.vertices:
        distance[u] = g.dijkstra(u)
        # back to original weights
        for v in g.vertices:
            distance[u][v] = distance[u][v] - h[u] + h[v]
    return distance


# testing code
if __name__ == "__main__":
    # Creating graph from CLRS #690
    g = DenseWeightedGraph(5)
    g.addEdge((0, 4, -4))
    g.addEdge((0, 1, 3))
    g.addEdge((2, 1, 4))
    g.addEdge((0, 2, 8))
    g.addEdge((1, 4, 7))
    g.addEdge((4, 3, 6))
    g.addEdge((3, 2, -5))
    g.addEdge((1, 3, 1))
    g.addEdge((3, 0, 2))
    g.print()

    distance = fastDPAlgo(g)
    print ("\nShortest path distances by BASIC DP ALGORITHM:")
    printMatrix(distance, g.v)

    distance = floydWarshall(g)
    print ("\nShortest path distances by FLOYD-WARSHALL ALGORITHM:")
    printMatrix(distance, g.v)


    sparseGraph = SSSP()
    for i in range(5):
        sparseGraph.addVertex(i)
    sparseGraph.addDirectedEdge((0, 4, -4))
    sparseGraph.addDirectedEdge((0, 1, 3))
    sparseGraph.addDirectedEdge((2, 1, 4))
    sparseGraph.addDirectedEdge((0, 2, 8))
    sparseGraph.addDirectedEdge((1, 4, 7))
    sparseGraph.addDirectedEdge((4, 3, 6))
    sparseGraph.addDirectedEdge((3, 2, -5))
    sparseGraph.addDirectedEdge((1, 3, 1))
    sparseGraph.addDirectedEdge((3, 0, 2))

    distance = johnson(sparseGraph)
    print ("\nShortest path distances by JOHNSON ALGORITHM:")
    printMatrix(distance, len(distance))
