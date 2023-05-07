T = int(input())

for t in range(1, T+1):
    N = int(input())
    d = [[0] * N for _ in range(N)]
    d[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                d[i][j] = 1
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j]

    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            if d[i][j]:
                print(d[i][j], end=' ')
        print()