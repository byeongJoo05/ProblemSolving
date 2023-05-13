T = int(input())
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, T+1):
    N = int(input())
    arr = []
    for coin in coins:
        arr.append(N//coin)
        N = N % coin

    print("#{}".format(t))
    print(*arr)