from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저들어온 순서
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) #나중에 들어온 순서

queueList = []
queueList = list(queue)
print(queueList)