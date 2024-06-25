# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deque = deque()
for _ in range(n):
    data = input().strip().split(" ")
    oper = data[0]

    if oper == '1':
        deque.appendleft(data[1])
    elif oper == '2':
        deque.append(data[1])
    elif oper == '3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif oper == '4':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif oper == '5':
        print(len(deque))
    elif oper == '6':
        if not deque:
            print(1)
        else:
            print(0)
    elif oper == '7':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif oper == '8':
        if deque:
            print(deque[-1])
        else:
            print(-1)