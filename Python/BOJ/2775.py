t = int(input())


for _ in range(t):
    k = int(input())
    n = int(input())
    zeroList = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            zeroList[j] += zeroList[j-1]

    print(zeroList[-1])