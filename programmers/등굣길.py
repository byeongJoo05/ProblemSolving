from collections import deque


def solution(m, n, puddles):
    dx = [1, 0]
    dy = [0, 1]
    answer = 0
    # n이 x, m이 y
    board = [[0 for _ in range(m)] for _ in range(n)]
    board[0][0] = 1
    for i, j in puddles:
        board[j - 1][i - 1] = -1
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if board[nx][ny] == -1:
                continue

            board[nx][ny] += board[x][y]
            if (nx, ny) not in queue:
                queue.append((nx, ny))

    answer = board[n - 1][m - 1] % 1000000007
    return answer