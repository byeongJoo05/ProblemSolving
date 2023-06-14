"""
양방향 그래프를 작성해서 풀어야 되는 문제였다.

양방향 그래프가 필요하므로
arr[i] += [j] 에 대한 배열을 만들어주고,
arr[j] += [i] 에 대한 배열을 만들어준다.

컴퓨터 1번부터 시작이므로 queue는 1부터 시작

그 후 BFS를 통해 visit 갯수를 세어주면 되는데,
로직상 +1 이 더 해지므로 정답에서 -1을 빼주면 된다.
"""

from collections import deque
n = int(input()) # 노드 갯수
v = int(input()) # 간선 갯수
visit = [0 for _ in range(n+1)] # 방문 배열
arr = [[] for _ in range(n+1)] # 그래프

for _ in range(v):
    i, j = map(int,input().split())
    arr[i] += [j]
    arr[j] += [i] # 양방향 노드 연결
visit[1] = 1
q = deque([1])

while q:
    x = q.popleft()
    for nx in arr[x]:
        if visit[nx] == 0:
            q.append(nx)
            visit[nx] = 1

print(sum(visit)-1)