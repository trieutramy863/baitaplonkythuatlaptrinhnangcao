# algorithms/bfs.py
# ===============================
# THUẬT TOÁN BFS
# ===============================

# algorithms/bfs.py

from collections import deque

def bfs_steps(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()

        # trả về trạng thái mỗi bước
        yield vertex, list(queue), list(visited)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)