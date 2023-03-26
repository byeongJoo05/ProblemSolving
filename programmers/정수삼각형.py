def solution(triangle):
    answer = 0
    n = int(len(triangle))
    print(n)
    d = [[0 for _ in range(n + 5)] for _ in range(1005)]
    d[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:  # 맨 왼쪽일때
                d[i][0] = triangle[i][0] + d[i - 1][0]
            elif i == j:
                d[i][j] = triangle[i][j] + d[i - 1][j - 1]
            else:
                d[i][j] = max(d[i - 1][j] + triangle[i][j], d[i - 1][j - 1] + triangle[i][j])

    answer = max(d[n - 1])
    return answer