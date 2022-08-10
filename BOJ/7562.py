from collections import deque
import sys
input = sys.stdin.readline

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

def bfs(nowX,nowY,moveX,moveY):
    queue = deque()
    queue.append((nowX,nowY))
    while queue:
        x, y = queue.popleft()
        if x == moveX and y == moveY:
            return graph[x][y] -1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >=0 and nx <l and ny <l and graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))



n = int(input())
for _ in range(n):
    l = int(input())
    nowX, nowY = map(int,input().split())
    moveX, moveY = map(int,input().split())
    graph=[[0]* l for _ in range(l)]
    graph[nowX][nowY]=1
    print(bfs(nowX,nowY,moveX,moveY))
