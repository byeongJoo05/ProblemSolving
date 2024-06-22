def solution(num_list):
    answer = 0
    
    total = 1
    sum = 0
    for i in num_list:
        total *= i
        sum += i
    
    if total > sum*sum:
        return 0
    else:
        return 1