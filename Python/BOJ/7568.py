n = int(input())

list = []

for _ in range(n):
    x, y = map(int, input().split())
    list.append((x,y))

for i in list:
    count = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            count+=1

    print(count, end=" ")