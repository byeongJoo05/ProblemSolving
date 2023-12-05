T = int(input())

for t in range(1, T+1):
    st = input()
    word = []
    cmp = []
    for i in range(11):
        word = st[:i]
        cmp = st[i:i*2]

        if i!=0 and word == cmp:
            ans = len(word)
            break

    print('#{} {}'.format(t, ans))