class DenseWeightedGraph:
    '''
        Class that represents a weighted directed graph using an adjacency matrix
        We assume the vertices are numbered from 0 to |V|-1
    '''
    def __init__(self, v):
        self.v = v
        # Adjacency matrix with diagonal entries 0, and everything else INF
        self.adj = [[float('inf') for i in range(self.v)] for i in range(self.v)]
        for i in range(self.v):
            self.adj[i][i] = 0

    def addEdge(self, edge):
        '''
            Args:
                edge: tuple (u, v, w) - directed edge from u to v of weight w
        '''
        u, v, w = edge
        if type(edge) != tuple or len(edge) != 3:
            raise Exception("Badly formatted edge. Expected tuple of length 3.")
        if u >= self.v or v >= self.v:
            raise Exception("Invalid vertices in the edge")
        self.adj[u][v] = w

    def print(self):
        print ("\nGraph Adjacency Matrix:")
        self.printMatrix(self.adj, self.v)

    def printMatrix(self, mat, n):
        '''
            Print square matrix "mat" of dimension n x n
        '''
        for i in range(n):
            print ("\t".join(map(str, mat[i])))


class APSP(DenseWeightedGraph):
    '''
        Class for solutions to all pairs shortest paths problems
        1. Basic DP Solution
        2. Floyd-Warshall
        3. Johnson
        We redefine the graph here as we need to use an adjacency matrix representation
        For Johnson's we still use an adjacency list so we can use the WeightedGraph class
    '''
    def fastDPAlgo(self):
        '''
            O(V^3*lgV) solution
        '''
        distance = self.adj
        m = 1
        while m < (self.v - 1):
            distanceUpdate = [[float('inf') for i in range(self.v)] for i in range(self.v)]
            for i in range(self.v):
                for j in range(self.v):
                    for k in range(self.v):
                        distanceUpdate[i][j] = min(distanceUpdate[i][j], distance[i][k] + distance[k][j])
            distance = distanceUpdate
            m = 2 * m
        print ("\nShortest path distances by BASIC DP ALGORITHM:")
        self.printMatrix(distance, self.v)

    def floydWarshall(self):
        '''
            O(V^3) solution
        '''
        distance = self.adj
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
        print ("\nShortest path distances by FLOYD-WARSHALL ALGORITHM:")
        self.printMatrix(distance, self.v)


# testing code
if __name__ == "__main__":
    # Creating graph from CLRS #690
    g = APSP(5)
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

    g.fastDPAlgo()
    g.floydWarshall()