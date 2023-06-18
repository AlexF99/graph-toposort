from graph import *
import sys

# input parsing
vertices = set()
edges = []
for line in sys.stdin:
    if '{' in line or '}' in line:
        continue
    if 'Exit' == line.rstrip():
        break
    edge = []
    iterator = filter(str.isalnum, line)
    for v in iterator:
        vertices.add(v)
        edge.append(v)
        if (len(edge) == 2):
            edges.append(tuple(edge))
            edge.pop(0)

vertices = list(vertices)

# build Graph
g = AdjMatrixGraph(len(vertices), vertices, edges, True)
print("\nmatriz:")
g.show_matrix()

# generate and print toposort list
sorted = g.topological_sort()
print("topological_sort: ")
print(sorted)