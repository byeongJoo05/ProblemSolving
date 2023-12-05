"""
그리디 문제.

시작 시간, 끝 시간

제일 많은 걸 고르려면 끝 시간으로 오름차순 정렬 이후 시작 시간으로 오름차순 정렬을 해야함.
-> 끝 시간으로만 하는 경우 시작 시간이 더 짧은 경우를 찾기가 어렵기 때문이다.

찾은 이후 끝시간을 한 변수에 저장하고나서 시작시간을 비교하며 짧은 것을 GET한다.
"""

import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x:(x[1],x[0]))

ans = 0
end = 0
for i in range(n):
    if arr[i][0] >= end:
        ans+=1
        end = arr[i][1]
print(ans)