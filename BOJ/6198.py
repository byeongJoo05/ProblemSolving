"""
빌딩은 오른쪽으로만 바라보게 됨.
만약 빌딩 높이가 높다면 자기보다 높은 위치 전까지 모든 빌딩을 확인할 수 있음
자신보다 높은 빌딩이 오른쪽에 있다면 볼 수 없다는 것도 일맥상통한 얘기임.
마지막 빌딩은 오른쪽 빌딩이 없기에 볼 수가 없지요.

정답값으로는 각 빌딩 당 볼 수 있는 빌딩 수의 총합임.

stack을 사용해서 어떻게 풀 수 있을까???

팝의 개수가 합이 된거라면?
"""
n = int(input())
building = []
stack = []
ans = 0
for _ in range(n):
    building.append(int(input()))


for i in building:
    while stack and stack[-1] < i: # 스택이 있어야 되고, 지금까지의 스택은 현재 높이보다 낮아야됨.
        stack.pop()
        ans+=1
    stack.append(i) # 끝엔 무조건 스택 추가

print(ans+1)