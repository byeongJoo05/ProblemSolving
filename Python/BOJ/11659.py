"""
d[i] = arr[1] + arr[2] + arr[3] + ... + arr[i]
d[i] = d[i-1] + arr[i]

배열 1~3 까지의 합을 구하려면
d[3] - d[0]

배열 2~4 까지의 합을 구하려면
d[4] - d[1] = arr[2] + arr[3] + ar[4]

시간초과 났음. fast io 도입해보기.
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

d = [0 for i in range(100005)]
arr = list(map(int, input().split()))

for i in range(1,n+1):
    d[i] = d[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int,input().split())
    print(d[j] - d[i-1])