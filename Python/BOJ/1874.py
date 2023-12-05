stack = []
n = int(input())
ans = []
pointer = 1
isStack = 1
for _ in range(n):
    num = int(input())
    while pointer<=num: # num이 될때 가지 push 하기
        stack.append(pointer)
        ans.append('+')
        pointer +=1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        isStack = 0
        break

if isStack == 1:
    for i in ans:
        print(i)