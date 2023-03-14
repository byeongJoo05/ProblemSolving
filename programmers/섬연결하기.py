"""
섬의 개수 = 정점의 개수
"""
import heapq  # 힙 선언


def solution(n, costs):
    answer = 0
    cnt = 0
    arr = [[] for _ in range(105)]  # 비용과 정점 번호를 저장할 배열

    check = [False for _ in range(105)]  # 정점 i가 최소신장트리에 속해 있는지를 위한 체크

    for i in costs:
        a, b, cost = i  # 정점(a,b), 가중치 꺼내주기.
        arr[a].append((cost, b))  # a 정점에 b정점 및 b정점과 연결한 가중치 추가
        arr[b].append((cost, a))  # b 정점에 a정점 및 a정점과 연결한 가중치 추가

    heap = []
    # 한 정점을 기준으로 하여 최소 신장트리 체크 하기.
    check[0] = True  # 정점 0으로부터 시작

    for nxt in arr[0]:
        heapq.heappush(heap, (nxt[0], 1, nxt[1]))  # 정점 0으로부터의 연결된 정점들과 가중치를 우선순위 큐에 삽입하기

    while cnt < n - 1:  # 간선의 개수가 모든 정점들의 합-1 때 까지.
        # 최소신장트리이기 때문에 간선의 개수는 정점의 개수보다 무조건 1개 적을 수 밖에 없다.
        cost, a, b = heapq.heappop(heap)  # 최소힙의 루트 노드 꺼내주기
        if check[b]:  # 만약 정점 b가 체크되어있다면? 건너뛰자.
            continue
        answer += cost  # 체크되어 있지 않다면, 현재 정점이 최소이므로 answer에 가중치를 덧셈
        check[b] = True  # 정점 b에 대한 연산을 잠그기
        cnt += 1  # 간선이 움직였으므로 간선 개수 추가
        for nxt in arr[b]:  # 정점 b로부터 뻗어나가기
            if not check[nxt[1]]:  # 정점 b로부터 a가 가중치 연산이 가능하다면
                heapq.heappush(heap, (nxt[0], b, nxt[1]))  # 우선순위큐(최소힙)에 정점 a,b 가중치 추가
    return answer