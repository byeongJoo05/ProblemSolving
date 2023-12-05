import heapq, sys

input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    num = int(input())

    if num == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)