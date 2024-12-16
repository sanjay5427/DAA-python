from collections import deque, defaultdict
import sys

def add_edge(graph, capacity, cost, u, v, cap, cst):
    graph[u][v] = cap
    graph[v][u] = 0
    capacity[u][v] = cap
    capacity[v][u] = 0
    cost[u][v] = cst
    cost[v][u] = -cst

def bfs(graph, cost, source, sink, parent):
    dist = {node: sys.maxsize for node in graph}
    in_queue = {node: False for node in graph}
    dist[source] = 0
    queue = deque([source])
    in_queue[source] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v in graph[u]:
            if graph[u][v] > 0 and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    return dist[sink] != sys.maxsize

def find_cycle_and_cancel(graph, capacity, cost, source, sink):
    max_flow = 0
    total_cost = 0
    parent = {}

    while bfs(graph, cost, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            total_cost += path_flow * cost[u][v]
            v = parent[v]

        max_flow += path_flow

    return max_flow, total_cost

# Get user input for the flow network
vertices = int(input("Enter the number of vertices in the flow network: "))
graph = defaultdict(lambda: defaultdict(int))
capacity = defaultdict(lambda: defaultdict(int))
cost = defaultdict(lambda: defaultdict(int))

edges = int(input("Enter the number of edges in the flow network: "))
print("Enter the edges with their capacities and costs in the format 'u v capacity cost':")
for _ in range(edges):
    u, v, cap, cst = input().split()
    cap = int(cap)
    cst = int(cst)
    add_edge(graph, capacity, cost, u, v, cap, cst)

source = input("Enter the source node: ")
sink = input("Enter the sink node: ")

# Calculate the minimum cost maximum flow from source to sink
max_flow, min_cost = find_cycle_and_cancel(graph, capacity, cost, source, sink)
print("The maximum possible flow is:", max_flow)
print("The minimum cost of the maximum flow is:", min_cost)
