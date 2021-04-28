from denseWeightedGraph import DenseWeightedGraph

# Solutions to all pairs shortest paths problems
# 1. Basic DP Solution
# 2. Floyd-Warshall
# 3. Johnson
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
    print ("\nShortest path distances by BASIC DP ALGORITHM:")
    g.printMatrix(distance, g.v)


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
    print ("\nShortest path distances by FLOYD-WARSHALL ALGORITHM:")
    g.printMatrix(distance, g.v)


def johnson(self):
    '''
        g is a weighted directed graph represented by an adjacency list - WeightedGraph
        (For Johnson's we use an adjacency list)
    '''
    pass


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

    fastDPAlgo(g)
    floydWarshall(g)