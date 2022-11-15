n = int(input())

dotList = []

for _ in range(n):
    x, y = map(int,input().split())
    dotList.append([x,y])

dotList.sort(key= lambda x:(x[0],x[1]))

for i, j in dotList:
    print(i,j)