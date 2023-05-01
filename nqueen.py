
N = int(input("Enter the number of queens:"))

board = [[0]*N for _ in range(N)]


def under_attack(i, j):

    for k in range(i):
        if(board[k][j] == 1):
            return True

    row = i-1
    col = j-1

    while(row >= 0 and col >= 0):
        if(board[row][col] == 1):
            return True
        row = row-1
        col = col-1

    row = i-1
    col = j+1

    while(row >= 0 and col < N):
        if(board[row][col] == 1):
            return True
        row = row-1
        col = col+1

    return False


def nqueen(n):

    if(n == 0):
        return True

    i = N-n
    for j in range(N):
        if(not(under_attack(i, j)) and board[i][j] != 1):
            board[i][j] = 1
            if(nqueen(n-1) == True):
                return True
            else:
                board[i][j] = 0

    return False


def main():
    nqueen(N)
    for i in board:
        print(i)


if __name__ == "__main__":
    main()
