import heapq


# Graph class to represent the weighted graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    # Method to add an edge with a weight
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Add v with weight
        self.graph[v].append((u, weight))  # Because it's an undirected graph

    # Dijkstra's Algorithm to find the shortest path
    def dijkstra(self, source):
        # Initialize distances and priority queue
        dist = {
            i: float("inf") for i in range(self.vertices)
        }  # Distance to all vertices
        dist[source] = 0  # Distance to source is 0
        parent = {i: None for i in range(self.vertices)}  # To store shortest path tree
        min_heap = [(0, source)]  # Priority queue (distance, vertex)

        while min_heap:
            # Get the vertex with the smallest distance
            current_dist, u = heapq.heappop(min_heap)

            # Skip if the node is already processed
            if current_dist > dist[u]:
                continue

            # Update the distance to each neighbor of u
            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight  # Update distance
                    parent[v] = u  # Update parent
                    heapq.heappush(min_heap, (dist[v], v))  # Add to the priority queue

        # Return distance and parent maps
        return dist, parent

    # Method to print the shortest path from the source to the destination
    def print_path(self, parent, destination):
        path = []
        while destination is not None:
            path.insert(0, destination)
            destination = parent[destination]
        return path


# Driver code to test Dijkstra's algorithm
if __name__ == "__main__":
    # Create a graph with 6 vertices (0-5)
    g = Graph(6)

    # Add edges (u, v, weight)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 10)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 5, 1)

    # Source node is 0
    source = 0
    dist, parent = g.dijkstra(source)

    print(f"Shortest distances from source node {source}:")
    for vertex in range(g.vertices):
        print(f"Distance to node {vertex}: {dist[vertex]}")

    print("\nShortest path from source node 0 to node 5:")
    path = g.print_path(parent, 5)
    print(" -> ".join(map(str, path)))
