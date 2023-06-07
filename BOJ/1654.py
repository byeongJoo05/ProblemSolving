import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

st, en = 1, max(arr)
while st <= en:
    line = 0
    mid = (st+en) // 2
    for i in arr:
        line += i // mid
    if line >= k:
        st = mid + 1
    elif line < k:
        en = mid - 1

print(en)