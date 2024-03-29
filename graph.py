import abc

class Graph(abc.ABC):
    def __init__ (self, num_vertices, vertices, edges, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.vertices = vertices
        self.edges = edges

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass
    
    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self, v):
        pass
   
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjMatrixGraph(Graph):
    def __init__(self, num_vertices, vertices, edges, directed=False):
        super(AdjMatrixGraph, self).__init__(num_vertices, vertices, edges, directed)
        self.matrix = self.zero_matrix(num_vertices)
        for e in edges:
            self.add_edge(self.vertices.index(e[0]), self.vertices.index(e[1]))

    def zero_matrix(self, num_vertices):
        matrix = []
        for i in range(num_vertices):
            line = []
            for j in range(num_vertices):
                line.append(0)
            matrix.append(line)
        return matrix

    def add_edge(self, v1, v2, weight=1):
        if self.matrix[v1][v2] > 0 or v1 == v2:
            return
        self.matrix[v1][v2] = weight
        if not self.directed: self.matrix[v2][v1] = weight
    
    def get_adjacent_vertices(self, v):
        adj_list = []
        index = 0
        for adjv in self.matrix[v]:
            if(adjv != 0):
                adj_list.append(index)
            index = index + 1
        return adj_list
    
    def get_indegree(self, v):
        indeg = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indeg += 1
        return indeg

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        pass

    def show_matrix(self):
        print(" ", end=" ")
        for v in self.vertices:
            print(f" {v}", end=" ")
        print()
        for i, line in enumerate(self.matrix):
            print(self.vertices[i], end=" ")
            print(line)
