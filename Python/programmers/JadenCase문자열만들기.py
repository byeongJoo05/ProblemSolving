def solution(s):
    answer = ''
    arr = list(s.split(" "))

    for word in arr:
        answer += word.capitalize() + " "
    answer = answer[:-1]
    print(answer)
    return answer