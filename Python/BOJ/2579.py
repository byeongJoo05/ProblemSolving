import sys

input = sys.stdin.readline

n = int(input())

d = [[0 for _ in range(3)] for _ in range(500)]
"""
IndexError 가 뜬다. arr 같아서 arr 초기값을 지정해주고 나서 풀어보겠다.
"""
arr = [0 for _ in range(305)]

for i in range(n):
    arr[i] = int(input())

d[1][1] = arr[0]
d[1][2] = 0
d[2][1] = arr[1]
d[2][2] = arr[0] + arr[1]

for k in range(3, n+1):
    d[k][1] = max(d[k-2][1], d[k-2][2]) + arr[k-1]
    d[k][2] = d[k-1][1] + arr[k-1]

if n == 1:
    print(arr[0])
    exit(0)
print(max(d[n][1], d[n][2]))