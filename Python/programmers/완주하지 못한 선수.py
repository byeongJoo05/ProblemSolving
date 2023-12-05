def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in completion:
        if i in dict:
            dict[i] -= 1

    for i in dict:
        if dict[i] >= 1:
            answer = i
    return answer