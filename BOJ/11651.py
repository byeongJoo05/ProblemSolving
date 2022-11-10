n = int(input())
locList = []
for _ in range(n):
    locList.append(list(map(int,input().split())))

locList.sort(key=lambda x: (x[1], x[0]))

for i in locList:
    print(i[0], i[1])