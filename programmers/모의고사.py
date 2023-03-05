"""
1번 사람은 -> 1 2 3 4 5 1 2 3 4 5... 등차수열로 오름
2번 사람은 -> 2 1 2 3 2 4 2 5 2 1 ... 2 다음 1,3,4,5 순으로 찍음
3번 사람은 -> 3 3 1 1 2 2 4 4 5 5 -> 3 1 2 4 5 순으로 패턴이 있으며, 한 숫자를 두 번씩 찍음
"""


def solution(answers):
    answer = []
    scores = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            scores[0] += 1
        if two[i % 8] == answers[i]:
            scores[1] += 1
        if three[i % 10] == answers[i]:
            scores[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx + 1)
    return answer