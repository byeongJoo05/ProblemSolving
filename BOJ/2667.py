from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
q = deque()
board=[]
hosu = 0
for _ in range(n):
    board.append(list(map(int, input())))
countList= []

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue

        q.append((i,j))
        board[i][j] = 0
        count = 1
        hosu += 1
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx <0 or nx>= n or ny <0 or ny>=n:
                    continue

                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))
                    count += 1

        countList.append(count)

countList.sort()

print(hosu)
for i in countList:
    print(i)