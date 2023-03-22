from itertools import product ,combinations_with_replacement
"""
반례 케이스
510 1
5
출력 : 5
정답 : 55
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
a = 1

for j in range(1, len(str(n))+1):
    for i in product(arr, repeat=j):
        tmp = ''.join(map(str, i))
        tmp = int(tmp)
        if tmp <= n:
            a = max(a, tmp)

print(a)