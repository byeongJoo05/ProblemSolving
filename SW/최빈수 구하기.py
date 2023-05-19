T = int(input())

for _ in range(T):
    dict = {}

    t = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        if not dict.get(i):
            dict[i] = 1
        else:
            dict[i] += 1

    print("#{} {}".format(t, max(dict, key=dict.get)))