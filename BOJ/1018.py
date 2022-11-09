n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(input()))

count = 0
for i in range(n-1):
    for j in range(m-1):
        if board[i][j] != board[i+1][j+1]:
            board[i+1][j+1] = board[i][j]
            count +=1
        if board[i][j] == board[i][j+1]:
            if board[i][j] == "B":
                board[i][j+1] = "W"
                count +=1
            elif board[i][j] == "W":
                board[i][j+1] = "B"
                count+=1
        if board[i][j+1] != board[i+1][j]:
            board[i+1][j] = board[i][j+1]
            count+=1

print(count)
