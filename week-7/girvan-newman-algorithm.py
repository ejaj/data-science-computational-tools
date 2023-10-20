import networkx as nx
import matplotlib.pyplot as plt

# Create a sample social network graph
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('D', 'E')])


def girvan_newman(G):
    communities = list(nx.connected_components(G))
    while len(communities) == 1:
        betweenness = nx.edge_betweenness_centrality(G)
        max_betweenness = max(betweenness, key=betweenness.get)
        G.remove_edge(*max_betweenness)
        communities = list(nx.connected_components(G))
    return communities


result = girvan_newman(G)
print("Communities:", result)
# Plot the graph with communities
pos = nx.spring_layout(G)
for i, community in enumerate(result):
    nx.draw_networkx_nodes(G, pos, nodelist=list(community), node_color=[i / len(result)] * len(community))
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
