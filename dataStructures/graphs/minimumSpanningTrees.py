from weightedGraph import WeightedGraph
from dataStructures.minPriorityQueue import MinPriorityQueue

class MST(WeightedGraph):
    def kruskalMST(self):
        '''
            Kruskal's Algorithm to find the MST
            Prints the MST array containing edges of an MST
        '''
        def findRoot(parent, v):
            '''
                Find operation of union-find with path compression
                Returns root of current node and updates parent of all nodes in path to the root
            '''
            if parent[v] != v:
                parent[v] = findRoot(parent, parent[v])
            return parent[v]

        def union(parent, rank, x, y):
            xRoot = findRoot(parent, x)
            yRoot = findRoot(parent, y)
            if rank[xRoot] < rank[yRoot]:
                parent[xRoot] = yRoot
            elif rank[xRoot] > yRoot:
                parent[yRoot] = xRoot
            else:
                parent[yRoot] = xRoot
                rank[xRoot] += 1

        MST = []

        # sort edges in non-decreasing order by weight
        sortedEdges = sorted(self.edges, key=lambda item: item[2])

        # arrays for union-find
        lenV = len(self.vertices)
        parent = [v for v in self.vertices]
        rank = [0] * lenV

        mstSize = 0							# iterator for the edges added to MST
        edge = 0							# iterator for the edges in sortedEdges
        while mstSize < (lenV-1):
            (u, v, w) = sortedEdges[edge]
            x = findRoot(parent, u)
            y = findRoot(parent, v)

            # if u and v belong to different subsets, add to MST by taking union
            if x != y:
                mstSize += 1
                MST.append(sortedEdges[edge])
                union(parent, rank, x, y)

            edge += 1

        # printing the MST
        print ("\nKruskal MST:")
        mstWeight = 0
        for edge in MST:
            u, v, w = edge
            print ("{} --- {} : {}".format(u, v, w))
            mstWeight += w
        print ("MST Weight: {}".format(mstWeight))


    def primMST(self):
        '''
            Prim's Algorithm to find the MST
            Prints the MST array containing edges of an MST
        '''

        lenV = len(self.vertices)

        # MST will contain edges (parent[i], i)
        parent = [-1] * lenV
        # to store the weight of the edge (parent[i], i) - to calculate MST weight
        weight = [0] * lenV
        # Initializing (key, vertex) tuples for the priority queue
        queueArray = []
        for v in self.vertices:
            queueArray.append((float('inf'), v))
        q = MinPriorityQueue(queueArray)
        # Initializing vertex 0 as root
        q.heapDecreaseKey(self.vertices[0], 0)

        while not q.isEmpty():
            _, u = q.heapExtractMin()
            for edge in g.adj[u]:
                v, w = edge
                if q.containsItem(v) and w < q.itemKey(v):
                    parent[v] = u
                    weight[v] = w
                    q.heapDecreaseKey(v, w)


        # printing the MST
        print ("\nPrim MST:")
        mstWeight = 0
        for i in range(1, lenV):
            print ("{} --- {} : {}".format(parent[i], i, weight[i]))
            mstWeight += weight[i]
        print ("MST Weight: {}".format(mstWeight))


# testing code
if __name__ == "__main__":
    g = MST()
    for i in range(9):
        g.addVertex(i)

    g.addUndirectedEdge((0, 1, 4))
    g.addUndirectedEdge((1, 2, 8))
    g.addUndirectedEdge((2, 3, 7))
    g.addUndirectedEdge((3, 4, 9))
    g.addUndirectedEdge((4, 5, 10))
    g.addUndirectedEdge((5, 6, 2))
    g.addUndirectedEdge((6, 7, 1))
    g.addUndirectedEdge((7, 0, 8))
    g.addUndirectedEdge((1, 7, 11))
    g.addUndirectedEdge((2, 8, 2))
    g.addUndirectedEdge((8, 7, 7))
    g.addUndirectedEdge((8, 6, 6))
    g.addUndirectedEdge((2, 5, 4))
    g.addUndirectedEdge((3, 5, 14))

    g.print()
    g.kruskalMST()
    g.primMST()
