"""
약간 투포인터 넉김처럼 푸는 문제. 범위를 구하기 위해서? -> 투포인터 ㄹㅇ 잘 알아놔야겠다.
보드의 중간 인덱스를 먼저 구해놓는다.

이제 행, 열을 기준으로 배열 탐색을 한다.
열은 mid를 기준으로 l, r 으로 크기를 점차 키운다.
행이 커진다면 l은 점차 좌측으로, r은 점차 우측으로 키운다.
행이 mid 보다 커진다면 l은 점차 우측으로, r은 점차 좌측으로 줄인다.
"""

T = int(input())

for t in range(1, T+1):
    n = int(input())
    board = []
    ans = 0

    for _ in range(n):
        l = list(input())
        board.append(list(map(int, l)))
    mid = n // 2
    l, r = mid, mid

    for i in range(n):
        for j in range(l, r+1):
            ans += board[i][j]
        if i < mid:
            l -= 1
            r += 1
        else:
            l += 1
            r -= 1

    print("#{} {}".format(t, ans))