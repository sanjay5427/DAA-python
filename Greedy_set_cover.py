def greedy_set_cover(universe, subsets):
    uncovered = set(universe)
    cover = []

    while uncovered:
        # Find the subset that covers the most uncovered elements
        best_subset = max(subsets, key=lambda s: len(s & uncovered))
        cover.append(best_subset)
        uncovered -= best_subset

    return cover

# Get user input for the universe and subsets
universe = set(map(int, input("Enter the elements of the universe (space-separated): ").split()))
num_subsets = int(input("Enter the number of subsets: "))
subsets = []
print("Enter each subset as space-separated elements:")
for _ in range(num_subsets):
    subset = set(map(int, input().split()))
    subsets.append(subset)

# Find the greedy set cover
set_cover = greedy_set_cover(universe, subsets)
print("Set Cover:")
for s in set_cover:
    print(s)