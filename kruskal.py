from disjoint_set import DisjointSet
import networkx as nx
import operator
import matplotlib.pyplot as plt

G = nx.Graph()
disjoint_set = DisjointSet(['a', 'b', 'c', 'd'])
node_set = disjoint_set.get()
#  GRAFO DI INPUT
i = 0
j = 2
for n in node_set:
    G.add_node(n[0], pos=(i, j))
    j = j-i
    i = i+1

G.add_edge('a', 'b', weight=2)
G.add_edge('a', 'c', weight=10)
G.add_edge('b', 'c', weight=9)
G.add_edge('b', 'd', weight=1)
G.add_edge('d', 'a', weight=3)
edges = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')


#  KRUSKAL
t = list()
KruskalG = nx.Graph()
#  Ordinamento degli archi
sorted_edges = sorted(edges.items(), key=operator.itemgetter(1))
for uv in sorted_edges:
    u = uv[0][0]
    v = uv[0][1]
    if disjoint_set.find(u) != disjoint_set.find(v):
        disjoint_set.union(u, v)
        t.append(uv)
        KruskalG.add_edge(u, v, weight=uv[1], color='b')
    else:
        KruskalG.add_edge(u, v, weight=uv[1], color='r')


edgesK = KruskalG.edges()
colors = [KruskalG[u][v]['color'] for u, v in edgesK]
weights = [KruskalG[u][v]['weight'] for u, v in edgesK]

plt.subplot(121)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges)
plt.subplot(122)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges)
nx.draw(KruskalG, pos, edges=edgesK, edge_color=colors)
plt.show()

