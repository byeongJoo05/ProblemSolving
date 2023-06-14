"""
최소 힙, 최대 힙의 요소 싱크로를 맞춰주어야 하는 문제.

싱크로를 맞춰주기 위해 i 요소의 사용 유무가 가장 중요함.
"""

import heapq

n = int(input())

for _ in range(n):
    m = int(input())
    minheap = []
    maxheap = []
    chk = [False for _ in range(m)]
    for i in range(m):
        oper, num = input().split()
        print(chk)
        if oper == "I":
            heapq.heappush(minheap, (int(num), i))
            heapq.heappush(maxheap,(int(num)*-1, i))
            chk[i] = True

        elif oper == "D":
            if int(num) == 1: # 최대값 삭제
                while maxheap and not chk[maxheap[0][1]]: # 첫 최대값을 꺼내올 수 있을 때까지, 쓰레기 값 버리기
                    heapq.heappop(maxheap)
                if maxheap : # 만약 maxheap이 남아있다면 이것이 최대값이므로
                    chk[maxheap[0][1]] = False
                    heapq.heappop(maxheap)
            else: # 최소값 삭제
                while minheap and not chk[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    chk[minheap[0][1]] = False
                    heapq.heappop(minheap)

    while minheap and not chk[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not chk[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if maxheap and minheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print("EMPTY")