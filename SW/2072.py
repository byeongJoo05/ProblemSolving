num = int(input())
numList = []
for _ in range(num):
    numList.append(list(map(int, input().split())))

sum = 0
for i in range(len(numList)):
    for j in numList[i]:
        if j%2 != 0:
            sum+=j
    print("#"+str(i+1)+" "+str(sum))
    sum = 0