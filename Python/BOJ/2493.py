"""
현재 값과 비교하여 지금까지 돌렸을 때 자신보다 낮은 탑들은 pop 해주기
자신보다 높은 탑은 push
스택의 top을 이용해야함. top은 [-1]하면 나오지 않을까
"""
import sys
input = sys.stdin.readline
n = int(input())
tower = list(map(int, input().split()))
stack = []
ans = []
for i in range(n):
    while stack:
        if tower[stack[-1][1]] < tower[i]:
            stack.pop()
        else:
            ans.append(stack[-1][1]+1)
            break
    else:
        ans.append(0)
    stack.append([tower[i],i])

for i in ans:
    print(i, end=" ")