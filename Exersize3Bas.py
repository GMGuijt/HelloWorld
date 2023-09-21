import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import random

TotalNodes = 50

def main(TotalNodes):
    """Main function foor creating the network"""
    Network = CreateNetwork()
    for i in range(5,TotalNodes):
        Addnode(i,Network)
        print(i)
    print('start fillup')
    FillUp(Network)
    nx.draw(Network,node_size = 5)
    plt.show()

def CreateNetwork():
    """Creates a network with a total of five nodes"""
    Network = nx.star_graph(4)
    return Network
Network = CreateNetwork()

def CountEdges(Network,node):
    """Counts the amount of edges a node has"""
    count = 0
    for node2 in range(len(Network)):
        a = nx.number_of_nodes(Network)
        count += Network.number_of_edges(node,node2)
    return count

def AddEdges(Network,node):
    """Add edges to a node"""
    #Forloop for calculating pi and plotting the edge
    for i in range(len(Network)-1):
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
    return Network

def FillUp(Network):
    count = 0
    nodes = range(TotalNodes)
    while nx.number_of_edges(Network) < 2*TotalNodes:
        node,node1 = nodes(random.randint(0,len(nodes))),nodes(random.randint(0,len(nodes)))
        if node == node1:
            continue
        edges_node = CountEdges(Network,node)
        edges_node1 = CountEdges(Network,node1)
        if edges_node<4 and edges_node1<4:
            Network.add_edge(node,node1)
            print('added note')
        elif edges_node1 == 4:
            nodes.pop()
        count += 1

def Addnode(node,Network):
    """Creates a new node and adds al neccecary edges"""
    Network.add_node(node)
    AddEdges(Network,node)
main(TotalNodes)