n = int(input())

d = [[0 for _ in range(n+5)] for _ in range(1005)]
arr = [0 for _ in range(1005)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

d[0][0] = arr[0][0]

"""
1. 한방에 해결하는 법 코드를 짰지만, 예시만 운으로 맞추고, 실패.

2. 맨 왼쪽. 중간. 맨 오른쪽으로 다시 시도.
"""
for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 맨 왼쪽
            d[i][0] = d[i-1][0] + arr[i][0]

        elif j == i: # 맨 오른쪽
            d[i][j] = d[i-1][j-1] + arr[i][j]

        else: # 중간
            d[i][j] = max(d[i-1][j] + arr[i][j], d[i-1][j-1] + arr[i][j])


print(max(d[n-1]))