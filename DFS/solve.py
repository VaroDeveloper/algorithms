import networkx as nx
from simple_stack import Stack

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """

    N = graph.number_of_nodes()
    
    visible_nodes = set()
    order = {}  
    topo_order = []  
    S = Stack() 
    
    def dfs_iterative(start_node):
        S.push((start_node, False))
    
        while not S.isEmpty():
            node, processed = S.pop()
    
            if node not in visible_nodes:
                if not processed:
                    S.push((node, True))
                    for neighbor in graph.neighbors(node):
                        if neighbor not in visible_nodes:
                            S.push((neighbor, False))
                else:
                    visible_nodes.add(node)
                    topo_order.append(node)

    for node in graph.nodes():
        if node not in visible_nodes:
            dfs_iterative(node)
    
    for i, node in enumerate(reversed(topo_order), start=1):
        order[node] = i

    return order
