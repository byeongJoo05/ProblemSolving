T = int(input())

for t in range(1, T+1):
    N = int(input())
    ans = 0
    speed = 0
    for _ in range(N):
        c = list(map(int, input().split()))

        if c[0] == 1:
            speed += c[1]
        elif c[0] == 2:
            if speed < c[1]:
                speed = 0
            else:
                speed -= c[1]

        ans += speed

    print("#{} {}".format(t, ans))