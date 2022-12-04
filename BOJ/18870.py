from bisect import bisect_left

n = int(input())
xList = list(map(int, input().split()))

targetList = sorted(list(set(xList)))

ans = []
for i in xList:
    a = bisect_left(targetList, i)
    ans.append(a)

print(*ans)