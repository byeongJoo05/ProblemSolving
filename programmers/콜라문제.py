"""
콜라 빈 병 2개? -> 콜라 1병 (단, 보유 중인 빈 병 2개 미만? -> 콜라 없어)
DP 인가?

콜라가 짝수 개 -> 나누기 2
콜라 홀수 개 -> ?

20 -> 10(10) -> 5(5) -> 2(2) -> 1(1) -> 0(1)

1. 실제 콜라 개수와 빈 병 개수를 생각해서 해보기.
"""

# 빈병 a개를 주면 콜라 b 병을 줌. 초기 빈병 n 개를 가져다 주면 몇 병 줌?
# 빈병이 2개 미만이면 계산 하면 안됨
def solution(a, b, n):
    answer = 0
    coke = 0
    while True:
        if n < 2 or n < a:
            break
        answer += (n//a) * b
        # print("answer = ", answer)
        n = (n//a) * b + (n%a) # 돌아온 빈 병 갯수도 b만큼 증가해야되니 넣어줘야됨.
        # print("n = ", n)
    return answer