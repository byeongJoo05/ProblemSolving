n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
a.sort()
b.sort()
for i in a:
    st, en = 0, len(b) - 1
    flag = True
    while st <= en:
        mid = (st+en) //2

        if i > b[mid]:
            st = mid + 1
        elif i < b[mid]:
            en = mid - 1
        elif i == b[mid]:
            flag = False
            break
    if flag:
        ans.append(i)

print(len(ans))
print(*ans)