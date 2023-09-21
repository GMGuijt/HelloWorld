import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
def CreateNetwork():
    """Creates a network with a total of five nodes"""
    Network = nx.star_graph(4)
    return Network
Network = CreateNetwork()

def CountEdges(Network,node):
    """Counts the amount of edges a node has"""
    count = 0
    for node2 in range(len(Network)):
        count += Network.number_of_edges(node,node2)
    return count

def AddEdges(Network,node):
    """Add edges to a node"""
    for i in range(len(Network)):
        if CountEdges(Network,i) == 4:
            continue
        di = CountEdges(Network,i)
        dj = 0
        for j in range(node-1):
            dj += CountEdges(Network,j)
        pi = di/dj
        if sp.binom.rvs(1,pi) == 1:
            Network.add_edge(node,i)
        if CountEdges(Network,node) == 4:
            break
    print(pi)
    return Network
    
def Addnode(node,Network):
    """Creates a new node and adds al neccecary edges"""
    Network.add_node(node)
    AddEdges(Network,node)

def main():
    Network = CreateNetwork()
    for i in range(5,50):
        Addnode(i,Network)
    nx.draw(Network,node_size = 5)
    plt.show()
main()
