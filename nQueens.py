N = int(input("Number of queens: "))

board = [[0] * N for _ in range(N)]

def is_attack(row, col):
    for i in range(0, N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True

    for i in range(0, N):
        for j in range(0, N):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return True
    return False

def N_queen(row):
    if row == N:
        return True
    for col in range(N):
        if not is_attack(row, col):
            board[row][col] = 1
            if N_queen(row + 1):
                return True
            board[row][col] = 0
    return False

if N_queen(0):
    for row in board:
        for x in row:
            print('Q' if x == 1 else '.', end=" ")
        print()
else:
    print("There is no solution")
