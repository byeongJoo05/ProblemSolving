from collections import deque

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for t in range(1, T+1):
    N = int(input())
    q = deque([(0,0)])
    board = []
    visit = [[10005 for _ in range(N)] for _ in range(N)]
    visit[0][0] = 0
    for _ in range(N):
        arr = list(map(int, input()))
        board.append(arr)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx <0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visit[nx][ny] > board[nx][ny] + visit[x][y]:
                visit[nx][ny] = board[nx][ny] + visit[x][y]

                q.append((nx,ny))
    print("#{} {}".format(t, visit[N-1][N-1]))