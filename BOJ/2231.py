n = int(input())

for i in range(1, n+1):
    num = i
    hap = i + sum(map(int, str(i)))

    if hap == n:
        print(i)
        break
else:
    print(0)