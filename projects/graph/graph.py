"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from typing import List, Set 
from pyannotate_runtime import collect_types
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id: int) -> None:
        """
        Mutates vertices dictionary by adding a new key with an empty value
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1: int, v2: int) -> None:
        """
        Add a directed edge to the graph.
        Note that assignment adds, it does not replace
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) #, self.vertices[v2].add(v1)
        else:
            return "Invalid edge, at least one of these does not exist"
    def add_undirected_edge(self, v1: int, v2: int) -> None:
        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2), self.vertices[v2].add(v1)
        else:
            return "Invalid edge, at least one of these does not exist"        

    def get_neighbors(self, vertex_id: int) -> Set[int]:
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex: int) -> None:
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited_nodes: Set = set()
        while q.size() > 0:
            curr = q.dequeue()
            if curr not in visited_nodes:
                print(curr)
                visited_nodes.add(curr)
                for neighbor in self.get_neighbors(curr):
                    q.enqueue(neighbor)
        # print(visited_nodes)
        # return visited_nodes

    def dft(self, starting_vertex: int) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited_nodes: Set = set()
        while s.size() > 0:
            curr = s.pop()
            if curr not in visited_nodes:
                print(curr)
                visited_nodes.add(curr)
                for neighbor in self.get_neighbors(curr):
                    s.push(neighbor)
       # print(visited_nodes)
       # return visited_nodes

    # helper function to get around not modifying dft_recursive arguments

    def DFT_visited_tracker(self, starting_vertex: int, visited: List[bool]) -> None:
        
        visited[starting_vertex] = True
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if visited[neighbor] == False:
                self.DFT_visited_tracker(neighbor, visited)

    def dft_recursive(self, starting_vertex: int) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = (len(self.vertices) + 1)  * [False]
        self.DFT_visited_tracker(starting_vertex, visited)
        
    def bfs(self, starting_vertex: int, destination_vertex: int) -> List[int]:
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order. Basically same as BFTraversal
        Except we stop once we find our destination
        And we have to store the paths in a list
        """
        q = Queue() 
        q.enqueue([starting_vertex]) # store start as a list element
        visited_nodes: Set = set()
        while q.size() > 0:
            path = q.dequeue() 
            curr = path[-1] # last node from path, addition from BFT
            if curr not in visited_nodes:
                visited_nodes.add(curr)
                if curr == destination_vertex: # stop cond, addition from BFT
                    return path
                for neighbor in self.get_neighbors(curr):
                    # addition from BFT, create new path and add neighbor to new path list
                    new_path = list(path) 
                    new_path.append((neighbor))
                    q.enqueue(new_path)

    def dfs(self, starting_vertex: int, destination_vertex: int) -> List[int]:
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited_nodes: Set = set()
        while s.size() > 0:
            path = s.pop()
            curr = path[-1]
            if curr not in visited_nodes:
                visited_nodes.add(curr)
                if curr == destination_vertex:
                    return path 
                for neighbor in self.get_neighbors(curr):
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex: int, destination_vertex: int) -> List[int]:
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print(graph.get_neighbors(1)) # Should print {2}


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
    print("BFT TEST")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT TEST")
    graph.dft(1)
    print("DFT RECURSE TEST")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS path")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS path")
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
