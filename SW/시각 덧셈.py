T = int(input())

for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h = 0
    m = 0

    m = m1 + m2
    dh, dm = divmod(m, 60)
    h = (h1 + h2 + dh) % 12

    if h == 0 :
        h = 12
    print('#{} {} {}'.format(t, h, dm))