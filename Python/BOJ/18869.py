"""
우주의 개수 M
우주에 있는 행성의 개수 N
"""
import bisect
import sys
input=sys.stdin.readline

m, n = map(int, input().split())
arr = []

for _ in range(m):
    l = list(map(int, input().split()))
    li = []
    for i in l:
        li.append(bisect.bisect_left(l,i))
        li.append(bisect.bisect_right(l,i))
    arr.append(li)

left = 0
right = 1
ans = 0
length = len(arr[0])
while left < len(arr) and right < len(arr):
    # if arr[left] == arr[right]: 속도 미침. 코테에서 쓰다가 큰일남.
    #     ans += 1
    flag = True
    for i in range(length):
        if arr[left][i] != arr[right][i]:
            flag = False
            break
    if flag:
        ans+=1

    right += 1

    if right == len(arr):
        left += 1
        right = left + 1

print(ans)