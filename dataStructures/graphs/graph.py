class Graph:
    '''
        We maintain the attribute "adj" as a dictionary of adjacency lists
        The attribute "vertices" is the list of all vertices in the graph

        Use addVertex() and addEdge() to update these
        Vertices have no other data except index, hence they are just ints
    '''

    def __init__(self):
        self.adj = {}
        self.vertices = []


    def addVertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            self.adj[v] = []
        else:
            print ("WARNING: Duplicate vertex added. Skipping...")


    def addEdge(self, edge):
        if type(edge) != tuple or len(edge) != 2:
            raise Exception("Badly formatted edge. Expected tuple of length 2.")

        if edge[0] not in self.vertices or edge[1] not in self.vertices:
            raise Exception("Edge between non-existing vertices. Please add vertex first.")

        self.adj[edge[0]].append(edge[1])


    def print(self):
        print ("\nGraph:")
        for u in self.adj:
            print ("{} : {}".format(u, self.adj[u]))
