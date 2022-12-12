import sys
sys.setrecursionlimit(10000)
cnt = 0
def recur(n, r, c):
    global cnt
    if n == 0:
        return cnt

    line = 2**(n-1)

    if r < line and c < line :
        recur(n - 1, r, c)
        return cnt

    elif r < line and c >= line :
        recur(n - 1, r, c - line)
        cnt += line * line
        return cnt

    elif r >= line and c < line:
        recur(n - 1, r - line, c)
        cnt += 2 * (line * line)
        return cnt

    else:
        recur(n - 1, r - line, c - line)
        cnt += 3 * (line * line)
        return cnt





n, r, c = map(int, input().split())
print(recur(n, r, c))