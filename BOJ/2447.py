import sys
sys.setrecursionlimit(10000)

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
def recur(n, x, y):
    if n == 1 :
        board[x][y] = "*"
        return

    offset = n//3
    recur(offset, x, y)
    recur(offset, x, y+offset)
    recur(offset, x, y+offset*2)
    recur(offset, x+offset, y)
    recur(offset, x+offset, y+offset*2)
    recur(offset, x+offset*2, y)
    recur(offset, x+offset*2, y+offset)
    recur(offset, x+offset*2, y+offset*2)

recur(n,0,0)
for x in range(n):
    for y in range(n):
        if board[x][y] == 0:
            board[x][y] = ' '

for i in board:
    print("".join(i))