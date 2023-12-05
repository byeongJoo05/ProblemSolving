from collections import deque

t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(board, q):
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >=n or ny <0 or ny>=m:
                continue

            if board[nx][ny] == 0:
                continue

            board[nx][ny] = 0
            q.append((nx,ny))


for _ in range(t):
    m, n, k = map(int, input().split()) # m이 열, n이 행
    board = [[0]* m for _ in range(n)]
    q = deque()
    count = 0
    for _ in range(k):
        y, x = map(int,input().split())
        board[x][y] = 1

    for x in range(n):
        for y in range(m):
            if board[x][y] != 0:
                q.append((x,y))
                bfs(board, q)
                count += 1

    print(count)
