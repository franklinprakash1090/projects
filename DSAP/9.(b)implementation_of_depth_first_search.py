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

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()  # Set to keep track of visited nodes

        visited.add(start)  # Mark the node as visited
        print(start, end=" ")  # Process the node (printing it)

        # Recur for all the unvisited neighbors
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Driver code to test DFS
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

print("DFS Traversal starting from node 1:")
graph.dfs(1)
