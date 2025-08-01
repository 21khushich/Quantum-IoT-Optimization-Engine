import networkx as nx

def create_random_network(num_devices=10, connection_prob=0.3):
    """
    Generates a random undirected IoT network graph.
    """
    G = nx.erdos_renyi_graph(n=num_devices, p=connection_prob)
    return G
