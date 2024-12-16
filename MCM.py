def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]

# Get user input for the matrices
def get_dimensions():
    matrices = int(input("Enter the number of matrices: "))
    dimensions = []
    for i in range(matrices):
        rows = int(input(f"Enter the number of rows for matrix {i + 1}: "))
        cols = int(input(f"Enter the number of columns for matrix {i + 1}: "))
        dimensions.append(rows)
        if i == matrices - 1:
            dimensions.append(cols)
    return dimensions

dimensions = get_dimensions()
min_cost = matrix_chain_order(dimensions)
print("The minimum number of multiplications needed is:", min_cost)
