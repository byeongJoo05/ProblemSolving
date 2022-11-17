"""
현재 값과 비교하여 지금까지 돌렸을 때 자신보다 낮은 탑들은 pop 해주기
자신보다 높은 탑은 push
스택의 top을 이용해야함. top은 [-1]하면 나오지 않을까
"""

n = int(input())
tower = list(map(int,input().split()))
stack = [(0,0)]
ans = []
for i in range(n):
    while stack: #스택이 빌 때까지 연산
        # 첫 값은 6, 0
        tower_height, tower_idx = stack.pop()
        print(tower_height)
        print(tower[i])
        if tower_height > tower[i]:
            ans.append(tower_idx+1)
            stack.append((tower, tower_idx))
            break
        else:
            continue
    else:
        ans.append(0)
    stack.append((tower[i],i))

print(*ans)