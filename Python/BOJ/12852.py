"""
바킹독 연습문제 풀기.

혼자 힘으로 맞추게 아님.

1. 테이블 정의
이번 dp 테이블은 최소 연산 횟수가 됨.
따른 dp 로, dp 테이블에서 연결 리스트처럼 넘어갈 위치에 대한 정보를 담음. => pre 테이블

2. 점화식
dp[i] = dp[i-1] + 1
pre[i] = i - 1

사실 이번 점화식에 관해서는 이해가 잘 안감. 아마 두 테이블의 연관성 때문이라고 봄.

3. 초기값 설정
dp[1] = 0, pre[1] = 0


"""

n = int(input())

dp = [0 for _ in range(10**6 + 3)]
pre = [0 for _ in range(10**6 + 3)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i - 1

    # 2로 나누는 것이 가능하다면?
    if i % 2 == 0 and (dp[i] > dp[i//2] + 1):
        dp[i] = dp[i//2] + 1
        pre[i] = i//2

    # 3으로 나누는 것이 가능하다면?
    if i % 3 == 0 and (dp[i] > dp[i//3] + 1):
        dp[i] = dp[i//3] + 1
        pre[i] = i//3


print(dp[n])
while True:
    print(n, end=" ")
    if n == 1:
        break
    n = pre[n]