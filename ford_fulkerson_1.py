from collections import defaultdict

# Helper function to perform BFS and find an augmenting path
def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = [source]
    visited.add(source)
    
    while queue:
        u = queue.pop(0)
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:  # Residual capacity should be positive
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

# Ford-Fulkerson algorithm to find the maximum flow
def ford_fulkerson(graph, source, sink):
    residual_graph = defaultdict(lambda: defaultdict(int))
    
    # Initialize the residual graph with original capacities
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] = capacity
    
    parent = {}  # To store the path
    max_flow = 0
    
    while bfs(residual_graph, source, sink, parent):
        # Find the maximum flow in the augmenting path
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parent[v]
        
        # Update the residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# Example graph with capacities
graph = {
    'S': {'A': 10, 'B': 5},
    'A': {'B': 15, 'T': 10},
    'B': {'T': 10},
    'T': {}
}

source = 'S'
sink = 'T'

print("The maximum possible flow is:", ford_fulkerson(graph, source, sink))