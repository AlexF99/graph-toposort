from graph import *
from queue import Queue

g = AdjMatrixGraph(8, True)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

g.add_edge(5, 6)
g.add_edge(5, 7)

print("\nmatriz:")
g.show_matrix()

def topological_sort(graph: Graph):
    zerodeg = Queue()
    indegree_map = {}
    sorted_list = []
    for v in range(graph.num_vertices):
        indegree_map[v] = graph.get_indegree(v)
        if indegree_map[v] == 0:
            zerodeg.put(v)
    
    while not zerodeg.empty():
        v = zerodeg.get()
        sorted_list.append(v)
        adjlist = graph.get_adjacent_vertices(v)
        for adj in adjlist:
            indegree_map[adj] = indegree_map[adj] - 1
            if indegree_map[adj] == 0:
                zerodeg.put(adj)

    if len(sorted_list) < g.num_vertices:
        print("graph has directed cycle")
    return sorted_list

sorted = topological_sort(g)
print("topological_sort: ")
print(sorted)