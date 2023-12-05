from collections import deque

n = int(input())

arr = list(map(int, input().split()))

stack = []

answer = deque()

arr.reverse()

for i in arr:
    if stack:
        while stack[-1] <= i:
            stack.pop()
            if not stack:
                break

        if stack and stack[-1] > i:
            answer.appendleft(stack[-1])
            stack.append(i)

    if not stack:
        answer.appendleft(-1)
        stack.append(i)

for i in answer:
    print(i, end=" ")
