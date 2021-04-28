from weightedGraph import WeightedGraph
from dataStructures.minPriorityQueue import MinPriorityQueue

class SSSP(WeightedGraph):
    '''
        Class for single-source shortest paths solutions for weighted directed graphs
        1. Bellman-Ford - for graphs with negative weights
        2. Dijkstra - for graphs with non-negative weights
        3. ssspInDAG - for weighted directed acyclic graphs
    '''
    def __init__(self):
        self.distance = None
        self.parent = None
        super().__init__()


    def _initializeSSSP(self, s):
        lenV = len(self.vertices)
        self.distance = [float('inf')] * lenV
        self.distance[s] = 0
        self.parent = [None] * lenV


    def _relax(self, u, v, w):
        if self.distance[v] > (self.distance[u] + w):
            self.distance[v] = self.distance[u] + w
            self.parent[v] = u


    def _printPaths(self, s):
        for v in self.vertices:
            if v == s:
                continue
            if self.distance[v] == float('inf'):
                # This vertex is not reachable
                print ("No path from {} to {}".format(s, v))
            else:
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

        # This is needed by Johnson's algorithm for apsp
        return self.distance


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

        # This is needed by Johnson's algorithm for apsp
        return self.distance


    def ssspInDag(self, s):
        topologicalSortedOrder = self.topologicalSort()
        self._initializeSSSP(s)
        for u in topologicalSortedOrder:
            for (v, w) in self.adj[u]:
                self._relax(u, v, w)



# testing code
if __name__ == "__main__":
    # Creating the graphs used to test the algorithm
    negativeWeightGraph  = SSSP()                   # for Bellman-Ford
    positiveWeightGraph = SSSP()                    # for Dijkstra
    dag = SSSP()

    for i in range(5):
        negativeWeightGraph.addVertex(i)
        positiveWeightGraph.addVertex(i)
        dag.addVertex(i)

    # Graph from CLRS #652
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

    # Graph from CLRS #659
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

    # Graph from CLRS #656
    dag.addVertex(5)                    # We added vertices 0-4 before
    dag.addDirectedEdge((0, 2, 2))
    dag.addDirectedEdge((1, 0, 5))
    dag.addDirectedEdge((0, 3, 6))
    dag.addDirectedEdge((1, 2, 3))
    dag.addDirectedEdge((2, 3, 7))
    dag.addDirectedEdge((3, 5, -1))
    dag.addDirectedEdge((2, 5, 4))
    dag.addDirectedEdge((2, 4, 2))
    dag.addDirectedEdge((5, 4, -2))
    dag.addDirectedEdge((3, 4, 1))

    print ("\nBELLMAN FORD")
    print ("============")
    negativeWeightGraph.print()
    negativeWeightGraph.bellmanFord(0)
    print ("\nOutput: ")
    negativeWeightGraph._printPaths(0)
    print ("\n----------------------------------------------")

    print ("\nDIJKSTRA")
    print ("========")
    positiveWeightGraph.print()
    positiveWeightGraph.dijkstra(0)
    print ("\nOutput: ")
    positiveWeightGraph._printPaths(0)
    print ("\n----------------------------------------------")

    print ("\nSSP IN DAG")
    print ("==========")
    dag.print()
    dag.ssspInDag(0)
    print ("\nOutput: ")
    dag._printPaths(0)
    print ("\n----------------------------------------------")
