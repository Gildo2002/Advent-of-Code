import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

array =  np.loadtxt('Input/Day09.txt',dtype=str,delimiter=',')
x,y = np.shape(array)
lista = []

G = nx.Graph()

for i in array:
    if i[0] not in lista:
        G.add_node(i[0])

for i in array:
    G.add_edge(i[0],i[1],weight = int(i[2]))

for i in G.edges(data=True):
    print(i)

#walk =  nx.all_shortest_paths(G,source="Tristram",target="Arbre",weight='weight')
walk = nx.dfs_edges(G,"Tristram")

for i in walk:
    print(i)

print(nx.shortest_path_length(G,source="Tristram",target="Arbre",weight='weight'))
# print(lista)

# for i in range(x):
#     print(array[i][0])
#        
