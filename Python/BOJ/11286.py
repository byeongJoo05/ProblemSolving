import heapq
import sys
input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    x = int(input())

    if x != 0 :
        heapq.heappush(heap,(abs(x),x)) # (1, 1), (1,-1)
    else:
        if heap:
            i = heapq.heappop(heap)[1]
            print(i)
        else:
            print(0)