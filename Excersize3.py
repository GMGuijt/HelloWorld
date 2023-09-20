import networkx as nx
import matplotlib.pyplot as plt
import random

alpha = 0
n0 = 5

def d(node):
    """counts the number of edges connected to the given node"""
    sum = 0
    for i in range(len(g)):
        sum += g.number_of_edges(node,i)
    return sum

def p(node):
    """calculates the chance of a new page to link to the given page"""
    count = 0
    for i in range(len(g)-1):
        count+=d(i)
    d(node)/count

g = nx.star_graph(n0)
wanted_size = 7
while len(g) < wanted_size:
    total = len(g)
    g.add_note(len(g))
    while d(total+1) < 4:
        for i in len(g):
            if g.number_of_edges(i,total+1) == 0:
                if random.random > p(i):
                    g.add_edge(i,total+1)

nx.draw(g)
plt.show()