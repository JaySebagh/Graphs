"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex): # breadth first travel
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first vertex
            vertex = queue.dequeue()
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited
                print(vertex)
                visited.add(vertex)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex): # depth first travel
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while stack.size() > 0:
            # Pop the first vertex
            vertex = stack.pop()
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited...
                print(vertex)
                visited.add(vertex)
                # Then add all of its neighbors to the top of the stack
                for i in self.vertices[vertex]:
                    stack.push(i)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # add starting to visited
        visited.add(starting_vertex)
        print("dft_recursion: ", starting_vertex)
        # loop over the neighbors
        for i in self.vertices[starting_vertex]:
            # if the neighbors arent in visited, call dft_recursive
            if i not in visited:
                self.dft_recursive(i, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
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
                if last_vertex == destination_vertex:
                  # IF SO, RETURN PATH
                  print("bfs: ", path)
                  return path
                # Mark it as visited...
                else:
                    visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.vertices[last_vertex]:
                  # COPY THE PATH
                  path_copy = path.copy()
                  # APPEND THE NEIGHOR TO THE BACK
                  path_copy.append(i)
                  # add copy to back of queue
                  queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        
        while stack.size() > 0:
            path = stack.pop()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    print("dfs: ", path)
                    return path
                else:
                    visited.add(last_vertex)
                for i in self.vertices[last_vertex]:
                    path_copy = path.copy()
                    path_copy.append(i)
                    stack.push(path_copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))