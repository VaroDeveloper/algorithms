import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    nodos_visibles = []
    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    distance[first_node] = 0
    Q = Queue()
    nodos_visibles.append(first_node)
    Q.enqueue(first_node);
    i = 0
    
    while not Q.isEmpty():
        node_act = Q.dequeue()

        for hijo in graph.neighbors(node_act):
            if distance[hijo] == infinite:
                distance[hijo] = distance[node_act] + 1
                Q.enqueue(hijo)


    return distance
