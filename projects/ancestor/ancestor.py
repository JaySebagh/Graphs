class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    # reverse the tuples
    # run a bredth first search on starting_node
    # if there aren't any paths, return -1
    # else return the longest path
        # else if there are multiple longest paths, return the one with smallest integer