def solution(n, arr1, arr2):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board2 = [[0 for _ in range(n)] for _ in range(n)]
    answer = []
    x = 0
    for i in arr1:
        bi = bin(i)[2:]  # 이진법으로 변환
        # n 개수만큼 0 채워주기
        biArr = list(map(int, str(bi)))

        while len(biArr) < n:
            biArr.insert(0, 0)
        y = 0
        for j in biArr:

            if j == 0:
                board[x][y] = " "
            elif j == 1:
                board[x][y] = "#"
            y += 1
        x += 1

    x = 0
    for i in arr2:
        bi = bin(i)[2:]  # 이진법으로 변환
        # n 개수만큼 0 채워주기
        biArr = list(map(int, str(bi)))

        while len(biArr) < n:
            biArr.insert(0, 0)
        y = 0
        for j in biArr:

            if j == 0:
                board2[x][y] = " "
            elif j == 1:
                board2[x][y] = "#"
            y += 1
        x += 1

    for i in range(n):
        idx = ""
        for j in range(n):
            if board[i][j] == "#" or board2[i][j] == "#":
                idx += "#"
            else:
                idx += " "
        answer.append(idx)

    return answer