from collections import deque

T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr = []

def bt(idx, x, y, num, board):
    num += board[x][y]

    if idx == 6:
        arr.append(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or ny<0 or nx >= 4 or ny >= 4:
            continue

        bt(idx+1, nx, ny, num, board)

for t in range(1,T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    arr = []
    q = deque()
    for i in range(4):
        for j in range(4):
            bt(0,i,j,"", board)

    ans = len(set(arr))

    print("#{} {}".format(t, ans))