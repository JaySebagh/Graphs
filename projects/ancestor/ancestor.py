class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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

    def bfa(self, starting_vertex): 
        path_list = []
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.vertices[last_vertex]:
                  # COPY THE PATH
                  path_copy = path.copy()
                  # APPEND THE NEIGHOR TO THE BACK
                  path_copy.append(i)
                  # add copy to back of queue
                  queue.enqueue(path_copy)
            path_list.append(path)
        return path_list


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()
    # reverse the tuples
    reversed_tuples = []
    for i in ancestors:
        reverse = i[::-1]
        reversed_tuples.append(reverse)
    # extract all the nodes (so we can use .add_vertex)
    all_vertexes = []
    for i in reversed_tuples:
        first = i[0]
        second = i[1]
        all_vertexes.append(first)
        all_vertexes.append(second)
    all_vertexes = list(dict.fromkeys(all_vertexes))
    # add ancestor nodes to graph
    for i in all_vertexes:
        ancestor_graph.add_vertex(i)
    # add ancestor edges to graph
    for i in reversed_tuples:
        ancestor_graph.add_edge(i[0], i[1])
    # run a bredth first traversal on starting_node
    bfa = ancestor_graph.bfa(starting_node)
    print(bfa)
    if len(bfa) == 1:
        return -1
    else:
        last = bfa[-1][-1]
        return last

    # if there aren't any paths, return -1
    # else return the longest path
        # else if there are multiple longest paths, return the one with smallest integer
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 3)