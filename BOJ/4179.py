"""
R : 행
C : 열

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
"""
from collections import deque
r, c = map(int,input().split())
board = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 지훈이 거리
dist1 = [[[0] * c] for _ in range(r)]
q1 = deque()
# 불 거리
dist2 = [[[0] * c] for _ in range(r)]
q2 = deque()

for _ in range(r):
    board.append(list(char for char in input()))

print(board)
for i in range(r):
    for j in range(c):
        if board[i][j] == "J":
            q1.append((i,j))
        if board[i][j] == "F":
            q2.append((i,j))
        if board[i][j] == ".":
            dist1[i][j] = -1
            dist2[i][j] = -1

# 지훈이 bfs
while q1:
    x, y = q1.popleft()
    for direction in range(4):
        nx = dx[direction]
        ny = dy[direction]

    if nx < 0 or nx >= r or ny < 0 or ny >= c:
        continue

    if dist1[nx][ny] >=0:
        continue

    dist1[nx][ny] = dist1[x][y] + 1
    q1.append((nx,ny))

# 불 bfs
while q2:
    x, y = q2.popleft()
    for direction in range(4):
        nx = dx[direction]
        ny = dy[direction]

    if nx < 0 or nx >= r or ny < 0 or ny >= c:
        continue

    if dist2[nx][ny] >= 0:
        continue

    dist2[nx][ny] = dist2[x][y] + 1
    q2.append((nx, ny))

print("IMPOSSIBLE")