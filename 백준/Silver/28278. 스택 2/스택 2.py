# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    oper = input().split()

    if oper[0] == '1':
        stack.append(oper[1])
    elif oper[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif oper[0] == '3':
        print(len(stack))
    elif oper[0] == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif oper[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)