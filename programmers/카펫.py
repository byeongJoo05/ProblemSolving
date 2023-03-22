"""
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다.

yellow 의 모습을 통해 brown 개수가 일치하는지 확인 해야 함.

출력은 또 brown 모습이므로 yellow의 모습을 통해 답을 출력해야함
"""


def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):  # i는 가로의 길이
        row = yellow // i  # 세로의 길이
        if yellow % i != 0:
            continue
        compr = 2 * (i + 2) + 2 * row
        if compr == brown and i >= row:
            answer.append(i + 2)
            answer.append(row + 2)
    return answer