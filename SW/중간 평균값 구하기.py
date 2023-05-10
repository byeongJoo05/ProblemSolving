T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    ans = round(sum(arr[1:-1])/len(arr[1:-1]))

    print("#{} {}".format(t, ans))