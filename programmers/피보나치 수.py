"""
피보나치 인줄 알았는데 dp 였던 문제.
재귀로 푸니 시간 초과 및 런타임 에러가 남
"""


def fibo(n):
    if n == 0 or n == 1:
        return n

    return fibo(n - 1) + fibo(n - 2)


def solution(n):
    d = [0 for _ in range(n + 5)]

    d[0] = 0
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1234567

    answer = d[n]
    return answer