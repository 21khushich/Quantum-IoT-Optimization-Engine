import matplotlib.pyplot as plt
import networkx as nx

def plot_network(G, title="IoT Network"):
    """
    Plots the given network graph using matplotlib.
    """
    plt.figure(figsize=(6,4))
    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray')
    plt.title(title)
    plt.show()
