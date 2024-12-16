def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def place_queens(board, col, n):
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = place_queens(board, col + 1, n) or res
            board[i][col] = 0

    return res

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    place_queens(board, 0, n)

n = int(input("Enter the value of N for the N-Queens problem: "))
solve_n_queens(n)
