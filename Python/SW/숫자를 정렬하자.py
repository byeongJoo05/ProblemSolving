T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    arr.sort()
    print("#{} ".format(t), end="")
    print(*arr)