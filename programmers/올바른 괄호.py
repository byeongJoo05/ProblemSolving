def solution(s):
    answer = True

    arr = list(s)

    stack = []

    for i in arr:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        answer = False

    return answer