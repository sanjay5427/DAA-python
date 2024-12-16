from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

# Get user input for the flow network
vertices = int(input("Enter the number of vertices in the flow network: "))
graph = Graph(vertices)

edges = int(input("Enter the number of edges in the flow network: "))
print("Enter the edges with their capacities in the format 'u v capacity':")
for _ in range(edges):
    u, v, capacity = map(int, input().split())
    graph.add_edge(u, v, capacity)

source = int(input("Enter the source node: "))
sink = int(input("Enter the sink node: "))

max_flow = graph.ford_fulkerson(source, sink)
print("The maximum possible flow is:", max_flow)
