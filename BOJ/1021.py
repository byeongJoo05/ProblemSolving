"""
이 큐에서 몇 개의 원소를 뽑아내려 함. -> 이게 m이겠죠?
큐에 처음에 포함되어 있던 수 N -> ???
두번째 배열은 원소위치
"""

import sys
from collections import deque

input= sys.stdin.readline
n, m = map(int,input().split())
mList = list(map(int,input().split()))
deque = deque(i for i in range(1,n+1))
sum = 0 # 연산횟수 -> 근데 이게 최솟값이 필요한 이유는??



for i in mList:
    while True:
        if i == deque[0]:
            deque.popleft()
            break
        else:
            if deque.index(i) <= len(deque)//2:
                #왼쪽으로 한 칸 이동
                deque.append(deque.popleft())
                sum += 1
            else :
                # 오른쪽으로 한 칸 이동
                deque.appendleft(deque.pop())
                sum += 1

print(sum)