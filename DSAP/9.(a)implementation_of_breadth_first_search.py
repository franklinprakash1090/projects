from collections import deque


# Graph class to represent a graph using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Queue for BFS
        visited.add(start)

        while queue:
            node = queue.popleft()  # Dequeue a node
            print(node, end=" ")  # Process the node (printing it)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)  # Enqueue unvisited neighbors


# Driver code to test BFS
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

print("BFS Traversal starting from node 1:")
graph.bfs(1)
