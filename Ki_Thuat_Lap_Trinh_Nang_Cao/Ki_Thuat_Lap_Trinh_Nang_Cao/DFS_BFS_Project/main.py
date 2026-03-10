# main.py
# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================

from demo.console_demo import run_demo
from graph.graph_data import graph
from visualization.draw_graph import draw_graph

def main():
    run_demo()

    show = input("Bạn có muốn minh họa đồ thị không? (y/n): ")
    if show.lower() == 'y':
        draw_graph(graph)

if __name__ == "__main__":
    main()
