import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    h, w, n = map(int,input().split())
    if n % h == 0: # XX1호
        x = h
        y = n // h
    else: # 그 외
        x = n % h
        y = (n//h)+1

    print(x*100+y)