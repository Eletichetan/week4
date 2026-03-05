import networkx as nx
import matplotlib.pyplot as plt

# Regions (variables)
regions = ['A', 'B', 'C', 'D']

# Colors assigned after CSP backtracking
color_map = {
    'A': 'red',
    'B': 'green',
    'C': 'blue',
    'D': 'red'
}

# Adjacency (constraints)
edges = [
    ('A','B'),
    ('A','C'),
    ('B','C'),
    ('B','D'),
    ('C','D')
]

# Create graph
G = nx.Graph()
G.add_nodes_from(regions)
G.add_edges_from(edges)

# Node colors
node_colors = [color_map[node] for node in G.nodes()]

# Draw graph
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=15,
    font_weight='bold'
)

plt.title("Map Colouring CSP Solution")
plt.show()