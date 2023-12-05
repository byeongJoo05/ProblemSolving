T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for t in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    dir = 0

    x = 0
    y = 0

    for i in range(1, N**2+1):
        board[x][y] = i
        nx = x+dx[dir]
        ny = y+dy[dir]
        if nx <0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] != 0:
            dir += 1
            if dir == 4:
                dir = 0

        x, y = x+dx[dir], y+dy[dir]

    print("#{}".format(t))
    for row in board:
        print(*row)