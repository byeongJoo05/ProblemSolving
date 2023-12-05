T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 행부터 돌리기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[i][j] == 0:
                if cnt == K: # board 순회 중 1의 길이가 끝났는데, cnt가 3이라면?
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K : # 행 바뀜이 일어나는데 cnt가 3이라면 정답 +1
            ans += 1

    # 열부터 돌리기
    for j in range(N):
        cnt = 0
        for i in range(N):
            if board[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            ans += 1

    print("#{} {}".format(t, ans))