from dataStructures.queues import Queue

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


    def topologicalSort(self):
        '''
            TopologicalSort using Kahn's algorithm for weighted graph
        '''
        inDegree = [0] * len(self.vertices)
        visitedCnt = 0
        topologicalSort = []

        for u in self.adj:
            for (v, _) in self.adj[u]:
                inDegree[v] += 1

        q = Queue(len(self.vertices))

        for u in self.vertices:
            if inDegree[u] == 0:
                q.enqueue(u)

        while not q.isEmpty():
            u = q.dequeue()
            topologicalSort.append(u)
            visitedCnt += 1

            for (v, _) in self.adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.enqueue(v)

        if visitedCnt != len(self.vertices):
            raise Exception("Topological Sort not possible, cycle found")

        return topologicalSort


    def print(self):
        print ("\nGraph:")
        for u in self.adj:
            print ("{} : {}".format(u, self.adj[u]))
