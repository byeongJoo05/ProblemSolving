n = int(input())
gameRule = ['3','6','9']

for i in range(1, n+1):
    count = 0
    for j in str(i):
        if j in gameRule:
            count += 1
    if count > 0:
        i = '-' * count
    print(i, end=' ')