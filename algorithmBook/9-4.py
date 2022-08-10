INF = int(1e9)

n, m = map(int, input().split())

graph=[[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: # 자기 자신으로 가는 비용은 0
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1  # A->B, B->A 가는 비용은 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dist = graph[1][k] + graph[k][x] # 1번 노드에서 부터 x까지 가는 거리를 계산한 거리(=dist)

if dist >= INF:
    print("-1")
else:
    print(dist)