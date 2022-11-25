import math

while True:
    a = list(map(int, input().split()))
    maxNum = max(a)
    if sum(a) == 0 :
        break

    a.remove(maxNum)
    if math.pow(a[0],2) + math.pow(a[1],2) == math.pow(maxNum, 2):
        print("right")
    else:
        print("wrong")