
# gui/gui_app.py
# ==================================================
# GUI + ANIMATION DFS / BFS (STEP / STACK / QUEUE)
# ==================================================

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

from graph.graph_data import graph

# -------------------------------
# Tạo đồ thị
# -------------------------------
G = nx.DiGraph()
for u in graph:
    for v in graph[u]:
        G.add_edge(u, v)

pos = nx.spring_layout(G)

# -------------------------------
# GUI APP
# -------------------------------
class DFSBFSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DFS / BFS Animation Demo")
        self.geometry("950x650")

        self.steps = []
        self.container = []
        self.visited = []
        self.index = 0
        self.mode = None

        self.create_widgets()
        self.create_canvas()
        self.draw_graph([])

    # ---------------------------
    def create_widgets(self):
        top = ttk.Frame(self)
        top.pack(pady=5)

        ttk.Label(top, text="Start node:").grid(row=0, column=0, padx=5)
        self.start_node = ttk.Combobox(top, values=list(graph.keys()), width=5)
        self.start_node.set("A")
        self.start_node.grid(row=0, column=1)

        ttk.Button(top, text="DFS", command=self.prepare_dfs).grid(row=0, column=2, padx=5)
        ttk.Button(top, text="BFS", command=self.prepare_bfs).grid(row=0, column=3, padx=5)

        ttk.Button(top, text="Step", command=self.step).grid(row=0, column=4, padx=5)
        ttk.Button(top, text="Auto", command=self.auto_run).grid(row=0, column=5, padx=5)
        ttk.Button(top, text="Reset", command=self.reset).grid(row=0, column=6, padx=5)

        self.info = tk.StringVar()
        ttk.Label(self, textvariable=self.info, font=("Consolas", 12)).pack(pady=5)

    # ---------------------------
    def create_canvas(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    # ---------------------------
    def draw_graph(self, visited):
        self.ax.clear()

        colors = []
        for node in G.nodes():
            if node in visited:
                colors.append("red")
            else:
                colors.append("lightblue")

        nx.draw(
            G, pos,
            ax=self.ax,
            with_labels=True,
            node_color=colors,
            node_size=2000,
            font_size=12,
            arrows=True
        )

        self.ax.set_title("DFS / BFS Animation")
        self.canvas.draw()

    # ---------------------------
    def prepare_dfs(self):
        self.mode = "DFS"
        start = self.start_node.get()
        self.steps, self.container = self.dfs_steps(start)
        self.reset(run=True)

    def prepare_bfs(self):
        self.mode = "BFS"
        start = self.start_node.get()
        self.steps, self.container = self.bfs_steps(start)
        self.reset(run=True)

    # ---------------------------
    def dfs_steps(self, start):
        visited = set()
        steps = []
        stack_log = []

        def dfs(u, stack):
            visited.add(u)
            steps.append(u)
            stack_log.append(stack.copy())

            for v in graph[u]:
                if v not in visited:
                    stack.append(v)
                    dfs(v, stack)
                    stack.pop()

        dfs(start, [start])
        return steps, stack_log

    def bfs_steps(self, start):
        visited = set([start])
        queue = deque([start])
        steps = []
        queue_log = []

        while queue:
            u = queue.popleft()
            steps.append(u)
            queue_log.append(list(queue))

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return steps, queue_log

    # ---------------------------
    def step(self):
        if self.index < len(self.steps):
            self.visited.append(self.steps[self.index])
            self.draw_graph(self.visited)

            structure = self.container[self.index] if self.index < len(self.container) else []
            self.info.set(f"{self.mode} | Visited: {self.visited} | "
                          f"{'Stack' if self.mode=='DFS' else 'Queue'}: {structure}")

            self.index += 1

    def auto_run(self):
        if self.index < len(self.steps):
            self.step()
            self.after(800, self.auto_run)

    def reset(self, run=False):
        self.visited = []
        self.index = 0
        self.draw_graph([])
        self.info.set("")
        if run:
            self.step()

# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    app = DFSBFSApp()
    app.mainloop()
