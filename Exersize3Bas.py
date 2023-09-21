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
    """Counts the amount of edges a node has:
    Takes:
        -The network and the node number
    Returns
        -The number of connections a node has"""
    count = 0
    for node2 in range(len(Network)):
        a = nx.number_of_nodes(Network)
        count += Network.number_of_edges(node,node2)
    return count

def AddEdges(Network,node):
    """Add edges to a node:
    Takes: 
        -a network and a note to add things to
    Returns:
        -A node whith some edges"""
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
    """Creates all remaining edges because i don't know what else to do to make all the nodes have 4 edges.
    Takes:
        -The Network which needs to be filled up
    Returns:
        -The filled up network with all the nodes having exactly 4 connections
    """
    count = 0
    nodes = list(range(TotalNodes))
    while nx.number_of_edges(Network) < 2*TotalNodes:
        node,node1 = nodes[random.randint(0,len(nodes))-1],nodes[random.randint(0,len(nodes))-1]
        if node == node1:
            continue
        edges_node = CountEdges(Network,node)
        edges_node1 = CountEdges(Network,node1)
        if edges_node<4 and edges_node1<4:
            Network.add_edge(node,node1)
            print('added note')
        elif edges_node1 == 4:
            nodes.remove(node1)
        else:
            nodes.remove(node)
        count += 1

def Addnode(node,Network):
    """Creates a new node and adds al neccecary edges
    Takes: 
        -node, which is the number of the node that's being added
    Returns
        -Adds the node number with the right connections
    """
    Network.add_node(node)
    AddEdges(Network,node)
main(TotalNodes)