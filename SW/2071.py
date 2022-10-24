num = int(input())
numList = []

for _ in range(num):
    numList.append(list(map(int,input().split())))

count = 0
sum = 0

for i in range(num):
    for j in numList[i]:
        count += 1
        sum += j
    print("#"+ str(i+1) + " "+ str(round(sum/count)))
    count=0
    sum=0