import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
minus_sum = 0
zero_sum = 0
plus_sum = 0
board = []
for _ in range(n):
    board.append(list(input().split()))

def recur(x, y, n):

    global minus_sum, zero_sum, plus_sum
    target = board[x][y]
    flag = True

    for i in range(x,x+n):
        for j in range(y, y+n):
            if board[i][j] != target:
                flag = False
                break
        if not flag:
            break

    if flag == True:
        if int(target) == 1:
            plus_sum += 1
        elif int(target) == 0:
            zero_sum += 1
        elif int(target) == -1:
            minus_sum += 1
        return

    offset = n // 3
    for i in range(3):
        for j in range(3):
            recur(x+offset*i, y+offset*j, offset)


recur(0, 0, n)
print(minus_sum)
print(zero_sum)
print(plus_sum)