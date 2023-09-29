import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Main function for creating the network"""
    Network = nx.DiGraph()
    Data,Dataset = load_data()
    CreateNodes(Network,Dataset)
    CreateEdges(Network,Data)
    nx.draw(Network,node_size = 10)
    plt.show()

def load_data():
    """Function that loads the data, and returns a dataframe with all the connections and a set of all the different nodes"""
    Data = pd.read_csv('squirrel_edges.csv')
    #First 2000 values because else the code is too slow
    Data = Data.head(2000)
    #Making a dataset with all the distinct node numbers
    d1 = list(Data['id1'])
    d2 = list(Data['id2'])
    Dataset = set(d1+d2)
    return Data,Dataset

def CreateNodes(Network,Dataset):
    """Function that creates all the nodes from 'Dataset' in the network"""
    a = len(Dataset)
    for node in Dataset:
        #for every node in Dataset, add node to network
        Network.add_node(node)
    return Network

def CreateEdges(Network,Data):
    """Function that creates all edges from 'Data' in the network"""
    for i in range(len(Data)):
        #for every row in the dataset, make an edge from d1 to d2
        Network.add_edge(Data['id1'].iloc[i],Data['id2'].iloc[i])
main()