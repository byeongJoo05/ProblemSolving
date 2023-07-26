def solution(k, score):
    answer = []

    minList = []

    for i in score:
        if len(minList) < k:
            minList.append(i)
        else:
            if min(minList) < i:
                minList.remove(min(minList))
                minList.append(i)
        answer.append(min(minList))
    return answer