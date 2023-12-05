"""
DP 와 투포인터를 합쳐서 푸는 문제가 아닌가 싶다.
이유 1 - 투포인터로 한다해도 리스트 슬라이싱으로 찾는경우 계속계속 자르면서 찾고하기 때문에 시간초과가 난다.

1. 첫 시도 - 걍 투포인터 + 리스트 슬라이싱

2. 두번째 시도 - 투포인터 + DP
"""


import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

right = 0

ans = int(1e9)
sum = arr[0]
for left in range(n):
    while right < n and sum < s:
        right += 1
        if right != n :
            sum += arr[right]

    if right == n:
        break
    ans = min(ans, right-left+1)
    sum -= arr[left]

if ans == int(1e9):
    print(0)
    exit(0)
print(ans)