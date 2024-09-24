import networkx as nx

def build_graph():
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear el grafo no-dirigido con sus vértices
    
    #Creamos el grafo
    graph = nx.Graph()

    #Añadimos los nodes al grafo con los valores 1,2,3(num_nodes = 5. Entonces range(1, num_nodes + 1) será range(1, 6), y el bucle iterará sobre los valores 1, 2, 3, 4 y 5,
    #añadiendo cada uno de estos como un nodo en el grafo.)
    for nodes in range(1, num_nodes + 1):
        graph.add_node(nodes)
        
    # Paso 2: Añadirle las aristas
    
    #Iteramos segun el numero de aristas que hay
    for _ in range(num_edges):
        
        #didvidimos la linea, el primer valor es el nodo de inicio y el segundo el nodo final de la arista
        line = input().split()
        node1 = int(line[0])
        node2 = int(line[1])
        
        #añadimos la arista
        graph.add_edge(node1, node2)

    return graph
