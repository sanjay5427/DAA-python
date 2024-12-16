def greedy_coloring(graph):
    # Initialize the result dictionary to store colors assigned to vertices
    result = {}

    # Assign colors to vertices one by one
    for vertex in graph:
        # Find the colors of adjacent vertices
        adjacent_colors = set(result[neighbor] for neighbor in graph[vertex] if neighbor in result)

        # Find the first available color
        color = 0
        while color in adjacent_colors:
            color += 1

        # Assign the found color to the current vertex
        result[vertex] = color

    return result

# Get user input for the graph
vertices = int(input("Enter the number of vertices in the graph: "))
edges = int(input("Enter the number of edges in the graph: "))

# Initialize the graph as an adjacency list
graph = {i: [] for i in range(vertices)}
print("Enter the edges in the format 'u v' (0-based index):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Perform greedy coloring
coloring = greedy_coloring(graph)

# Print the result
print("Vertex Colors:")
for vertex in coloring:
    print(f"Vertex {vertex}: Color {coloring[vertex]}")
