"""
숨바꼭질 1에서 가장 빠른 시간으로 찾는 방법이 추가됬네.


아이디어
nx == k 일 때, 카운트를 세주는 게 제일 나으려나?
if x == k : count += 1
이건 맞음

전에는 dist[k] == -1 로 while 돌렸는데, 지금은 못할듯?
- dist[k] == -1 이 조건식으로 쓰면 1번밖에 안찍힐 테니까.

한 번 방문 처리는 쉬웠지만, 다시 방문을 어떻게 잡아주는 게 나을까?
dist[nx] == dist[x] +1 이면 다시 들어갈 수 있게해줘야하나?
"""
from collections import deque

n, k = map(int, input().split())

dist = [-1] * 100002

q = deque()
dist[n] = 0
q.append(n)
count = 0 # 가장 빠른 시간으로 찾는 방법 카운트

while q:
    x = q.popleft()
    if x == k: # 지금 위치가 k 와 같다면 조건 성립.
        count += 1

    for i in (x-1, x+1, x*2):
        nx = i

        if nx < 0 or nx >100000:
            continue

        # if dist[nx] != -1: 이거 때문에 한 번 밖에 안찍히네. 근데 이거 없으면 일단 거리값이 꼬일 수 있다고 생각.
        #     continue

        if dist[nx] == -1:
            dist[nx] = dist[x] + 1 # 이 거 자체로 한 번 방문을 할 수 있음.
            q.append(nx)

        elif dist[nx] != -1 and (dist[nx] == dist[x] + 1): # 이미 방문은 했는데, 배열 다음 값이 현재 배열 +1 (=> 다음값) 과 같다면 q 삽입.
            q.append(nx)                                   # 경우의 수가 발생했다는 것이므로 큐 삽입

print(dist[k])
print(count)