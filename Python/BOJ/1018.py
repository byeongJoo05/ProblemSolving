n, m = map(int, input().split())

board = []
count = []
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        countW = 0
        countB = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) %2 == 0: # 짝수일 때
                    if board[a][b] != 'B':
                        countB +=1
                    if board[a][b] != 'W':
                        countW +=1
                else:
                    if board[a][b] !='W':
                        countB +=1
                    if board[a][b] !='B':
                        countW +=1
        count.append(countB)
        count.append(countW)

print(min(count))
