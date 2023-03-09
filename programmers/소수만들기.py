from itertools import combinations


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        k = sum(i)
        cnt = 0
        for i in range(2, k + 1):
            if k % i == 0:
                cnt += 1

        if cnt == 1:
            answer += 1

    return answer