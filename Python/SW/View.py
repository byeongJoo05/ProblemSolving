d = [-2,-1,1,2]

for t in range(1,11):
    N = int(input())

    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        now = arr[i]
        comMax = 0
        flag = True
        for j in range(4):
            if now > arr[i-d[j]]:
                if comMax < arr[i-d[j]]:
                    comMax = arr[i-d[j]]
            else:
                flag = False

        if flag:
            ans += (arr[i]-comMax)

    print("#{} {}".format(t, ans))