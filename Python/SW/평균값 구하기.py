T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))

    ans = round(sum(arr) / len(arr))

    print("#{} {}".format(t, ans))