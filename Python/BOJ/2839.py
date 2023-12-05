n = int(input())

sum = 0
while n >=0:
    if n==1 or n==2:
        print(-1)
        break

    if n % 5 == 0 :
        sum += (n//5)
        print(sum)
        break

    n -= 3
    sum += 1