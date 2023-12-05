"""
dp로 풀 수 있는 문제
"""


def solution(n):
    answer = 0
    dp = [0 for _ in range(n + 5)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    answer = dp[n]
    return answer