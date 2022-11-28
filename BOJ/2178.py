"""
1은 이동할 수 있는 칸.
0은 이동할 수 없는 칸.
0,0에서 거리가 1칸씩 멀어질수록 +1만큼씩 커짐.
내가 마지막으로 찾고 싶은 곳은 (n-1, m-1)
"""

from collections import deque

n, m = map(int,input().split())

board = []
dist = [[-1] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n):
    board.append(list(map(int, input())))

queue = deque()
queue.append((0,0)) # (1,1) 에서 출발하여
dist[0][0] = 1 # 첫번째 방문처리
while queue:
    x, y = queue.popleft()
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or nx >= n or ny <0 or ny>=m:
            continue
        if dist[nx][ny] >= 0 or board[nx][ny] != 1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))

print(dist[n-1][m-1]) # 첫 시작을 0부터 시작했자나~