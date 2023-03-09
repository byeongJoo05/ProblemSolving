"""
n 을 이진화 처리를 한 이후 1의 개수만 쏙쏙 센다.

n을 +1 해주면서 어느 수를 이진화 처리를 한 이후 1의 개수가 같다면 그 값을 다시 10진수화 시켜서
정답을 출력한다.
"""


def solution(n):
    binN = list(map(int, bin(n)[2:]))
    cnt = sum(binN)  # n의 1의 개수만 cnt를 세 줄 변수
    answer = 0

    i = n  # 증가연산을 시켜줄 i
    while True:
        i += 1

        binI = list(map(int, bin(i)[2:]))
        cntI = sum(binI)

        if cntI == cnt:
            answer = i
            break
    return answer