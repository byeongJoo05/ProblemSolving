T= int(input())

num = list(map(int, input().split()))

num.sort()

if T % 2 == 0 :
    print(num[T/2])
else:
    print(num[int((T-1)/2)])