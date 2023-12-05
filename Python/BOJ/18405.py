"""
N x N 크기 시험관

1번부터 K번까지의 바이러스 종류 중 하나에 속함

1초마다 상, 하, 좌, 우의 방향으로 증식

매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식

특정 칸에 어떤 바이러스가 존재 -> 갈 수 없음

S초가 지난 후 (X,Y) 에 존재하는 바이러스의 종류를 출력

S초가 지난 후 해당 위치에 바이러스가 없으면 0 출력

가장 왼쪽 위에 해당하는 곳은 1,1임

S초 뒤에 (X,Y) 에 존재하는 바이러스 종류 출력
"""

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, k = map(int, input().split())

board = []
first = []

for _ in range(n):
    board.append(list(map(int, input().split())))

s, a, b = map(int,input().split())

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            first.append((board[i][j],i,j,0))

first.sort()
queue = deque(first)

while queue:
    v, x, y, t = queue.popleft()

    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny <0 or nx >=n or ny >=n:
            continue

        if board[nx][ny] != 0:
            continue

        board[nx][ny] = v
        queue.append((v, nx, ny, t+1))

print(board[a-1][b-1])