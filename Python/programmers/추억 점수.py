def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for arr in photo:
        a = 0
        for i in arr:
            if i in dict:
                a += dict[i]
        answer.append(a)
    return answer