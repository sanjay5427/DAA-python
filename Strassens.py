import numpy as np

def split_matrix(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen_multiply(A, B):
    if A.shape[0] == 1:
        return A * B

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

def get_matrix_input(size):
    print(f"Enter the elements of the {size}x{size} matrix row by row (space-separated):")
    matrix = []
    for i in range(size):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != size:
            raise ValueError(f"Each row must have {size} elements.")
        matrix.append(row)
    return np.array(matrix)

def main():
    size = int(input("Enter the size of the matrices (must be a power of 2, e.g., 2, 4, 8, 16): "))
    if (size & (size - 1)) != 0 or size <= 0:
        raise ValueError("Size must be a power of 2 and greater than 0.")
    
    print("Matrix A:")
    A = get_matrix_input(size)
    print("Matrix B:")
    B = get_matrix_input(size)

    result = strassen_multiply(A, B)

    print("\nResultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
