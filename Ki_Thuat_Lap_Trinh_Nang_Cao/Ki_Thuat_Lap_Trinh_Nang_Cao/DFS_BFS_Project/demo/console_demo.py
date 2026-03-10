# demo/console_demo.py
# ===============================
# DEMO DFS / BFS (CONSOLE)
# ===============================

from graph.graph_data import graph
from algorithms.dfs import dfs
from algorithms.bfs import bfs

def run_demo():
    print("========== DFS / BFS DEMO ==========")
    print("1. Duyệt DFS")
    print("2. Duyệt BFS")

    choice = input("Chọn thuật toán (1 hoặc 2): ")

    if choice == '1':
        result = dfs(graph, 'A')
        print("Thứ tự DFS:", " -> ".join(result))

    elif choice == '2':
        result = bfs(graph, 'A')
        print("Thứ tự BFS:", " -> ".join(result))

    else:
        print("Lựa chọn không hợp lệ!")
