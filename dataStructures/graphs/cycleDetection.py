from dataStructures.graphs.graph import Graph

# METHOD 1 - Using recursionStack
def detectCycleHelper(g, visited, recStack, v):
    visited[v] = True
    recStack[v] = True

    for node in g.adj[v]:
        if not visited[node]:
            if detectCycleHelper(g, visited, recStack, node):
                return True
        elif recStack[node]:
            return True

    recStack[v] = False
    return False

def detectCycle(g):
    '''
        Args:
            g (Graph): graph with unweighted directed edges
        Returns:
            bool : if cycle present in g, returns True else False
    '''
    visited = [False] * len(g.vertices)
    recStack = [False] * len(g.vertices)

    for v in g.vertices:
        if not visited[v]:
            if detectCycleHelper(g, visited, recStack, v):
                return True
    return False


# METHOD 2 - Using Colors
def detectCycleColorsHelper(g, node, color):
    color[node] = "GREY"
    for neighbor in g.adj[node]:
        if color[neighbor] == "GREY":
            return True
        if color[neighbor] == "WHITE" and detectCycleColorsHelper(g, neighbor, color):
            return True
    color[node] = "BLACK"
    return False 

def detectCycleColors(g):
    color = ["WHITE"] * len(g.vertices)

    for node in g.vertices:
        if color[node] == "WHITE":
            if detectCycleColorsHelper(g, node, color):
                return True
    return False



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
    print ("Cycle present in graph? {}".format(detectCycleColors(g)))

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
    print ("Cycle present in graph? {}".format(detectCycleColors(g_cycle)))
