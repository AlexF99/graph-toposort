import abc

class Graph(abc.ABC):
    def __init__ (self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

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
    def __init__(self, num_vertices, directed=False):
        super(AdjMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = self.zero_matrix(num_vertices)
        print(self.matrix)

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
        for line in self.matrix:
            print(line)
