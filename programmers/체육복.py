def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    l = [1 for _ in range(n + 1)]
    rel = [0 for _ in range(n + 1)]
    for i in lost:
        l[i] = 0

    for i in reserve:
        rel[i] = 1

    for i in lost:
        if rel[i]:
            l[i] = 1
            rel[i] = 0

    for i in reserve:

        if i == n:
            if l[i - 1] == 0 and rel[i]:
                l[i - 1] = 1
            break

        if (l[i - 1] == 0 or l[i + 1] == 0) and rel[i]:
            if l[i - 1] == 0:
                l[i - 1] = 1
            elif l[i + 1] == 0:
                l[i + 1] = 1

    # print(l)
    answer = sum(l) - 1
    return answer