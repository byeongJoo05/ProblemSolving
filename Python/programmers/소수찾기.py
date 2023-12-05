"""
딱 봐도 에라토스테네스의 체 넉김
"""


def solution(n):
    answer = 0
    isprime = [False, False] + [True] * (n + 1)
    for i in range(2, n + 1):
        if isprime[i]:
            # print(i)
            answer += 1
            for j in range(i, n + 1, i):
                isprime[j] = False

    return answer