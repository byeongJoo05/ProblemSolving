def solution(a, b):
    answer = 0
    
    
    operand = int(str(a)+str(b))
    multi = 2 * a * b
    
    if operand >= multi:
        return operand
    else:
        return multi