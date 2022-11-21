import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    arr = input().split()

    if arr[0] == "push":
        queue.append(arr[1])

    if arr[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if arr[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    if arr[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

    if arr[0] == "size":
        print(len(queue))

    if arr[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)