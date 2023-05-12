T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    rsum = 0 # 행의 합
    csum = 0 # 열의 합
    ssum = 0 # 3 * 3 크기의 합
    ans = 0
    # 행 찾기
    for i in range(9):
        rsum = sum(arr[i])
        if rsum != 45:
            # print("슈웃")
            print("#{} {}".format(t, ans))
            break

    if rsum != 45:
        continue

    # 열 찾기
    for j in range(9):
        csum = 0
        for i in range(9):
            csum += arr[i][j]

        if csum != 45:
            # print("슈웃")
            print("#{} {}".format(t, ans))
            break
    if csum != 45:
        continue

    # 3 * 3
    for offset in range(0,9,3):
        ssum = 0
        for i in range(offset,offset+3):
            for j in range(offset,offset+3):
                ssum += arr[i][j]
        if ssum != 45:
            print("#{} {}".format(t, ans))
            break

    if ssum != 45:
        continue

    ans = 1
    print("#{} {}".format(t, ans))