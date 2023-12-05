import sys

sys.setrecursionlimit(10000)
# t = 테스트케이스
t = int(input())

cnt = 0
result = []
output = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    mat[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if mat[nx][ny] == 1:
            dfs(nx, ny)


for _ in range(t):
    m, n, k = map(int, input().split())

    mat = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        mat[y][x] = 1
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                cnt = 0
                dfs(i, j)
                result.append(cnt)

    output.append(len(result))
    result = []

for i in output:
    print(i)