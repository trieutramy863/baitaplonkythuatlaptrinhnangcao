# visualization/draw_graph.py
# ===============================
# MINH HỌA ĐỒ THỊ
# ===============================

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    G = nx.DiGraph()

    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=12,
        arrows=True
    )

    plt.title("Minh họa đồ thị DFS / BFS")
    plt.show()
