def minimum_vertex_cover(edges):
    cover = set()
    remaining_edges = set(edges)

    while remaining_edges:
        u, v = remaining_edges.pop()
        cover.add(u)
        cover.add(v)

        # Remove all edges incident to u or v
        remaining_edges = {edge for edge in remaining_edges if u not in edge and v not in edge}

    return cover

# Get user input for the graph
n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
edges = []
print("Enter the edges in the format 'u v' (0-based index):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

# Find the minimum vertex cover
vertex_cover = minimum_vertex_cover(edges)
print("Minimum Vertex Cover:", vertex_cover)