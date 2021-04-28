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
