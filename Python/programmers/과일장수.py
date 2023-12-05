"""
사과의 상태에 따라 1~ k 점까지 점수 분류 -> k점이 최상품, 1점이 쓰레기
사과 한 상자의 가격
    한 상자에 사과 m개 담기
    상자에 담긴 사과 중 가장 낮은 점수가 p 점이라면, 사과 한 상자의 가격은 p*m

최대 이익을 계산하기 (남는 사과 버려버려)
! 이익이 발생하지 않는다면 0으로 리턴

아이디어 생각
    score의 길이를 m으로 나눴을 시 딱 떨어지지 않는다면 작은 숫자부터 버리기 - 나머지값만큼 빼주기
    score의 길이보다 m이 크다면 0 리턴 해주기. - 이건 그냥 구현

    score.sort를 통해 오름차순 정렬을 해주고 값을 빼주면 되겠쥬
"""


def solution(k, m, score):
    answer = 0
    thr = len(score) % m  # 버릴 숫자
    score.sort()

    if len(score) < m:
        return 0

    if thr != 0:
        for _ in range(thr):
            del score[0]

    for i in range(0, len(score), m):
        answer += score[i] * m

    return answer