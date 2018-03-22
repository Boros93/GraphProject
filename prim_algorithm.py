import networkx as nx
import math as math
from fibonacci_heap import FibonacciHeap


def build_heap(V, k, heap):
    nodes_heap = dict()
    for v in V:
        nodes_heap[v] = heap.insert(k[v], v) # accetta due parametri, key e value. Key è la chiave e value è il nome
    return nodes_heap


def build_MST(G, node_set, s, weight):
    MST = nx.Graph()
    for v in node_set:
        u = G.node[v]['pred']
        if v == s:
            MST.add_node(v)
            continue
        if (u, v) in weight.keys():
            w = weight[u, v]
        else:
            w = weight[v, u]
        MST.add_edge(u, v, weight=w)
    return MST


def prim(graph, weight, source, nodes):
    s = source  # Sorgente
    node_set = nodes
    G = graph
    # Inizializzazione
    for v in node_set:
        G.node[v]['key'] = math.inf  # setto ogni peso a infinito
        G.node[v]['pred'] = ''  # pongo i pred a NIL
        G.node[v]['flag'] = False  # è stato visitato?
    G.node[s]['key'] = 0

    # CREAZIONE DELL'HEAP
    Q = FibonacciHeap()
    keys = nx.get_node_attributes(G, 'key')
    nodes_heap = build_heap(node_set, keys, Q)  # salvo i puntatori ai nodi

    # CALCOLO DEL MST
    while Q.total_nodes != 0:
        u = Q.extract_min().value
        adj = nx.all_neighbors(G, u)
        print('u: ', u)

        for v in adj:
            if (u, v) in weight.keys():
                w = weight[u, v]
            else:
                w = weight[v, u]
            if not (G.node[v]['flag']) and w < nodes_heap[v].key:
                Q.decrease_key(nodes_heap[v], w)
                G.node[v]['pred'] = u
        G.node[u]['flag'] = True

    return build_MST(G, node_set, s, weight)



