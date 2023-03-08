"""
1. 구현으로 시도
 중앙을 기점으로 0부터 중앙 -1 +1 -2 +2 ... 등 커지게 만들 예정
 중앙은 요소 1 이상이어야 함 -> 요소 0과 마지막 요소는 펠린드롬을 만들 수 없기 때문임.

 형식이 1차원 BFS 처럼 나왔지만, 인접한 동일한 문자에 대한 처리가 어려워져 뇌지컬 이슈로 실패함.

2. 구현으로 재시도
 위와 비슷하긴 한데, 2중 for문을 이용하여 문제 풀기
 왼쪽 0번째 문자 부터해서 오른쪽 끝번째 문자부터 -1 씩 비교..
 같을 때마다 count 증가
 만약 틀렸다면 오른쪽을 reset 시켜주고, cnt 는 0으로 다시 바꿔줌
"""


def solution(s):
    answer = 0

    size = len(s)

    for i in range(size):
        cnt = 0
        j = 0
        while True:
            if j >= size - i:
                break
            left = s[i + cnt]
            right = s[size - j - 1]

            j += 1
            if left == right:
                cnt += 1
            else:
                j -= cnt
                cnt = 0

        if cnt:
            if answer < cnt:
                answer = cnt

    return answer