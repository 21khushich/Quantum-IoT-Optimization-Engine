from src.iot_network import create_random_network
from src.visualization import plot_network

if __name__ == "__main__":
    G = create_random_network(num_devices=8)
    plot_network(G, "Sample IoT Network")
