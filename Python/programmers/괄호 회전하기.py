from collections import deque


def isCollect(k):
    cmp = []
    for i in k:
        cmp.append(i)
        if len(cmp) >= 2:
            if cmp[-2] == "[" and cmp[-1] == "]":
                cmp.pop()
                cmp.pop()
            elif cmp[-2] == "(" and cmp[-1] == ")":
                cmp.pop()
                cmp.pop()
            elif cmp[-2] == "{" and cmp[-1] == "}":
                cmp.pop()
                cmp.pop()

    if not cmp:
        return True
    else:
        return False


def solution(s):
    cnt = len(s)  # 회전 수
    if cnt % 2 != 0:  # 홀수면 짝이 안맞으니 무조건 0
        return 0
    k = deque(s)
    answer = 0

    for _ in range(cnt):
        if isCollect(k):
            answer += 1
        k.rotate(-1)

    return answer