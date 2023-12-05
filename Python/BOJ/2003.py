n, m = map(int, input().split())
arr = list(map(int, input().split()))

st, en = 0, 0
cnt = 0
ans = 0
while en <= len(arr):
    cmp = sum(arr[st:en])

    if cmp == m:
        ans +=1
        en +=1
    elif cmp > m:
        st += 1
    elif cmp < m:
        en += 1

print(ans)