import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] =0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, k, x =map(int, input().split())
graph= [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int , input().split())
    graph[a].append((b,1)) # 거리는 모두 1

dijkstra(x)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)


# 플로이드와샬로 풀다가 포기
# n, m, k, x = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for a in range(n+1):
#     for b in range(n+1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# dist = graph[
# count = 0
# for a in range(1, n+1):
#     for b in range(1 ,n+1):
#         if graph[a][b] == k:
#             count += 1
#
#
# if count == 0:
#     print("-1")
# else:
#     print(count)