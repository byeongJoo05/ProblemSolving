def solution(my_string):
    answer = []
    for i in my_string.strip().split(" "):
        if i != "":
            answer.append(i)
    return answer