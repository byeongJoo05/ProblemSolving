T = 10

for t in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))

    for _ in range(N):
        minv = min(arr)
        maxv = max(arr)
        minIdx = arr.index(minv)
        maxIdx = arr.index(maxv)

        arr[minIdx] += 1
        arr[maxIdx] -= 1

    ans = max(arr) - min(arr)

    print("#{} {}".format(t, ans))