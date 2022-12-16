n = int(input())

board = []
ans = []
for _ in range(n):
    board.append(list(input()))

def recur(x, y, n):
    global ans
    target = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if target != board[i][j]:
                offset = n // 2
                ans.append("(")
                recur(x, y, offset)
                recur(x, y+offset, offset)
                recur(x+offset, y, offset)
                recur(x+offset, y+offset, offset)
                ans.append(")")
                return

    ans.append(target)

recur(0,0,n)

answer = "".join(map(str,ans))

print(answer)