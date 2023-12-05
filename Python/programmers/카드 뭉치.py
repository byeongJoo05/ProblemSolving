def solution(cards1, cards2, goal):
    answer = []
    i, j = len(cards1), len(cards2)
    n = m = 0

    for word in goal:
        if n < i and cards1[n] == word:
            answer.append(cards1[n])
            n += 1
        if m < j and cards2[m] == word:
            answer.append(cards2[m])
            m += 1

    return 'Yes' if answer == goal else 'No'