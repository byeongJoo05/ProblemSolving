import sys

t = int(input())

for _ in range(t):
    arr = sys.stdin.readline().split()
    for j in arr:
        print(j[::-1], end=" ")
    print()