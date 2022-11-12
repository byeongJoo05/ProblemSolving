n = int(input())
numList = list(map(int, input().split()))
count = 0
for i in numList:
    if i == 1:
        continue
    isSosu = 1
    for j in range(2, i):
        if i % j == 0:
            isSosu = 0
            break
    if isSosu:
        count += 1
print(count)