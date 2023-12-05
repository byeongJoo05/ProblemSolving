T = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
arr = []

for t in range(1, T +1):
    m1, d1, m2, d2 = map(int, input().split())
    answer = 0
    for i in range(m1, m2):
        if m1 == i:
            answer += day[i] - d1 + 1
        else:
            answer += day[i]
    answer += d2

    print("#{} {}".format(t, answer))
