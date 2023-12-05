T = int(input())
arr = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for i in range(T):
    arr.append(int(input()))

for idx, n in enumerate(arr):
    print('#'+str(idx+1))
    board = [[0 for _ in range(n)] for _ in range(n)]

    x = 0
    y = 0
    dir = 0

    for i in range(1, n**2 +1):
        board[x][y] = i

        if x+dx[dir] < 0 or y+dy[dir] <0 or x+dx[dir] >= n or y+dy[dir] >=n or board[x+dx[dir]][y+dy[dir]] != 0:
            dir += 1
            if dir == 4:
                dir = 0

        x += dx[dir]
        y += dy[dir]

    for row in board:
        print(*row)