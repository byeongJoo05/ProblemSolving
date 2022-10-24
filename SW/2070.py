T = int(input())

for i in range(T):
    j, k = map(int,input().split())
    if j < k:
        operand = "<"
    elif j > k:
        operand = ">"
    else:
        operand = "="
    print("#"+str(i+1)+" "+operand)