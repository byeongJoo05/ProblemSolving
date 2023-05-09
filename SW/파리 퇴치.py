T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]

    arr = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += board[i+k][j+l]
            arr.append(cnt)

    print("#{} {}".format(t, max(arr)))