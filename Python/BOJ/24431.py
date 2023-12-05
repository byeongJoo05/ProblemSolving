"""
n = 데이터 갯수, L = 문자열 길이, F = 공통 접미사
"""

t = int(input())

for _ in range(t):
    n, L, F = map(int, input().split())
    data = list(input().split())
    dict = {}
    cnt = 0

    for i in data:
        if not i[L-F:] in dict:
            dict[i[L-F:]] = 1
        else:
            dict[i[L-F:]] += 1

    for i in dict.values():
        if i == 1:
            continue
        elif i >= 2 and i % 2 == 0:
            cnt += (i//2)
        elif i >=3 and i % 2 != 0:
            cnt += (i//2)

    print(cnt)