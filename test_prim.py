import networkx as nx
import math
import matplotlib.pyplot as plt
from fibonacci_heap import FibonacciHeap
from prim_algorithm import prim


def build_heap(V, k, heap):
    nodes_heap = dict()
    for v in V:
        nodes_heap[v] = heap.insert(k[v], v) # accetta due parametri, key e value. Key è la chiave e value è il nome
    return nodes_heap


G = nx.Graph()
# GRAFO DI INPUT
node_set = ('a', 'b', 'c', 'd')

G.add_node('a', pos=(0, 1), key=0)
G.add_node('b', pos=(2, 1), key=0)
G.add_node('c', pos=(1, 0), key=0)
G.add_node('d', pos=(1, 2), key=0)


G.add_edge('a', 'b', weight=2)
G.add_edge('a', 'c', weight=30)
G.add_edge('b', 'c', weight=90)
G.add_edge('d', 'b', weight=1)
G.add_edge('d', 'a', weight=3)
weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
edges = G.edges
s = 'a'

MST = prim(G, weight, s, node_set)

edgesMST = MST.edges()
weightMST = nx.get_edge_attributes(MST, 'weight')

# STAMPA DI G
plt.subplot(121)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw(G, pos, edges=edges)

# STAMPA DEL MST
plt.subplot(122)
nx.draw(MST, pos, with_labels=True)
nx.draw_networkx_edge_labels(MST, pos, edge_labels=weightMST)
nx.draw(MST, pos, edges=edgesMST)

plt.show()
