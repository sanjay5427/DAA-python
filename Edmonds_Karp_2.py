from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Reverse edge with 0 capacity for residual graph

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = {}  # Stores the path to reconstruct the augmenting path
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            # Find the bottleneck capacity along the augmenting path
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Update the capacities and reverse flows in the residual graph
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            # Add path flow to the overall flow
            max_flow += path_flow

        return max_flow

# Get user input for the flow network
vertices = int(input("Enter the number of vertices in the flow network: "))
graph = Graph(vertices)

edges = int(input("Enter the number of edges in the flow network: "))
print("Enter the edges with their capacities in the format 'u v capacity':")
for _ in range(edges):
    u, v, capacity = input().split()
    capacity = int(capacity)
    graph.add_edge(u, v, capacity)

source = input("Enter the source node: ")
sink = input("Enter the sink node: ")

# Calculate the maximum flow from source to sink
max_flow = graph.edmonds_karp(source, sink)
print("The maximum possible flow is:", max_flow)
