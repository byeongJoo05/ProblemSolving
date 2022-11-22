t= int(input())

arr = []

for _ in range(t):
    arr.append(input())

for line in arr:
    count = 0
    for i in line:
        if i == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            print('NO')
            break
    else:
        if count == 0:
            print('YES')
        else:
            print('NO')
