"""
투포인터 새로운 방식
양 끝에서 부터 찾는 방법
"""


def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:  # 양쪽에서 합쳤을 때 구명보트보다 작거나 같다면
            left += 1  # 왼쪽 증가
            right -= 1  # 오른쪽 증가
        else:  # 크다면?
            right -= 1  # 뚱이 쪽 감소

        answer += 1  # 뚱이는 혼자 타세요
    return answer