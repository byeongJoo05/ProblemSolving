from itertools import permutations


def solution(numbers):
    answer = []
    data = permutations(numbers, 2)

    for i in data:
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()  # 오름차순으로 담아 return
    return answer