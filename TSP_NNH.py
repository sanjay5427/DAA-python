def tsp_nearest_neighbor(graph, start):
    n = len(graph)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    current_city = start

    for _ in range(n - 1):
        nearest_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city] and graph[current_city][city] < min_distance:
                nearest_city = city
                min_distance = graph[current_city][city]
        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city

    tour.append(start)  # Return to the starting city
    return tour

# Get user input for the graph
n = int(input("Enter the number of cities: "))
print("Enter the distance matrix row by row (space-separated values):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Find the approximate TSP solution using Nearest Neighbor Heuristic starting from city A (index 0)
tour = tsp_nearest_neighbor(graph, 0)
print("Approximate TSP Tour:", tour)
