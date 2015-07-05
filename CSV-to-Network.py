#! /usr/bin/env python: CSV-to-Network

import pandas as pd, networkx as nx, matplotlib.pyplot as plt
from networkx.algorithms import bipartite


# Build lists of nodes and edges:

df = (pd.read_csv('tales-01.txt', header=None)
    .groupby(level=0)
    .apply(lambda x : pd.DataFrame ([[x.iloc[0,0],v] for v in x.iloc[0,1:]]))
    .reset_index(drop=True)
    .dropna()
    .rename_axis({0:'text',1:'word'},axis=1)
    )
edges = df.values.tolist()
nodes_0 = list(set(df['text'].values.tolist()))
nodes_1 = list(set(df['word'].values.tolist()))

# Build a bipartite graph:

B = nx.Graph()
B.add_nodes_from(nodes_0, bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(nodes_1, bipartite=1)
B.add_edges_from(edges)

# Project one side of the graph:

G = nx.projected_graph(B, nodes_1)
nx.draw(G, 
        pos=nx.spring_layout(G), 
        with_labels = True,
        node_color = '#00CCFF')

# Choose your output:
# plt.show()
plt.savefig("graphing.png", dpi=300)