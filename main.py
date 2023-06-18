from graph import *
import sys

# Processa input
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

# Constroi grafo
g = AdjMatrixGraph(len(vertices), vertices, edges, True)

# Gera ordenacao topologica
sorted = g.topological_sort()
n = len(sorted) - 1
for i, v in enumerate(sorted):
    if i == n:
        print(v, end="\n")
    else: print(v, end=" ")