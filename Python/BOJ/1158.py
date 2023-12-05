from collections import deque

n, k = map(int, input().split())

numList = []
queue = deque()

for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    numList.append(queue.popleft())

print("<",", ".join(str(i) for i in numList),">", sep="")