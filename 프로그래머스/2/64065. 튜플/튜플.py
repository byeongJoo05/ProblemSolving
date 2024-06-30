def solution(s):
    li = []
    answer = []
    for i in s.split("},"):
        li.append(i.replace("{","").replace("}","").split(","))
    
    li.sort(key = len)
    for i in li:
        for j in i:
            if not int(j) in answer:
                answer.append(int(j))
    return answer