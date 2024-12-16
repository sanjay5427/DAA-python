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

# Example usage
graph = Graph(8)  # Number of vertices in the given graph representation

# Add edges with capacities
graph.add_edge('S', 'v1', 26)
graph.add_edge('S', 'v2', 17)
graph.add_edge('S', 'v4', 37)
graph.add_edge('v1', 'v3', 20)
graph.add_edge('v1', 'v4', 10)
graph.add_edge('v2', 'v4', 20)
graph.add_edge('v2', 'v5', 15)
graph.add_edge('v3', 'v6', 22)
graph.add_edge('v3', 'v5', 10)
graph.add_edge('v3', 'v7', 18)
graph.add_edge('v4', 'v3', 35)
graph.add_edge('v4', 'v5', 15)
graph.add_edge('v5', 'v7', 34)
graph.add_edge('v6', 't', 48)
graph.add_edge('v6', 'v7', 20)
graph.add_edge('v7', 't', 30)

# Calculate the maximum flow from source 'S' to sink 't'
source = 'S'
sink = 't'
max_flow = graph.edmonds_karp(source, sink)
print("The maximum possible flow is:", max_flow)
