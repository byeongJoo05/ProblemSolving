def solution(str_list, ex):
    answer = ''
    
    for word in str_list:
        if word.find(ex) != -1:
            continue
        answer += word
    
    return answer