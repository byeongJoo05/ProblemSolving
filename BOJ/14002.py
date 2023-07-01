"""
반례 케이스
8
6 9 6 9 1 8 6 7

가장 긴 부분증가 수열이면서, 증가 수열 중 가장 '긴' 게 포인트.
"""

n = int(input())

a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n): # 현재 원소 요소에 대한 반복
    for j in range(i): # 현재 원소 요소보다 왼쪽의 요소와 비교
        if a[i] > a[j]: # 현재 원소가 이전 요소보다 크다면
            dp[i] = max(dp[i], dp[j]+1) # 왼쪽에서 가장 큰 요소보다 +1


"""
맨 우측에 가장 큰 수의 요소가 있는 것은 확실하므로
우측부터 큰 요소부터 작은요소로 값을 출력
"""
print(max(dp)+1)

cmp = max(dp) # 요소 값을 비교하기 위한 변수. 초기값으로는 가장 큰 요소를 찾는다.
ans = []
for i in range(n-1, -1, -1): # 배열 요소 가장 끝부터 0요소까지 감소하면서 구하기
    if cmp == dp[i]: # 비교 변수와 같은 dp를 찾았다면
        ans.append(a[i]) # ans에 값 저장
        cmp -=1 # 비교값은 떨어뜨리기

ans.reverse() # 큰 수부터 저장했으므로 출력에 맞게 배열 뒤집기
print(*ans)