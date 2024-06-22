def solution(a, b):
    answer = 0
    
    oddA = False if a % 2 == 0 else True
    oddB = False if b % 2 == 0 else True
    
    if oddA and oddB:
        answer = a ** 2 + b ** 2
    elif oddA or oddB:
        answer = 2*(a+b)
    else:
        answer = abs(a - b)  
    
    return answer