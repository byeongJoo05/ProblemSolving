from collections import deque

n, k = map(int,input().split())
k -= 1
queue = deque()
data = []
for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k):
        queue.append(queue.popleft())
    data.append(queue.popleft())

print("<"+", ".join(map(str,data))+">")