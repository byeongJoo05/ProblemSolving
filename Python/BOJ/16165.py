n, m = map(int, input().split())
dict = {}
ans = []
for _ in range(n):
    group = input()
    cnt = int(input())
    l = []
    for _ in range(cnt):
        l.append(input())

    l.sort()
    for i in l:
        dict[i] = group

for _ in range(m):
    member = input()
    chk = int(input())

    if chk:
        ans.append(dict.get(member))
    else:
        for name, group in dict.items():
            if member==group:
                ans.append(name)

for i in ans:
    print(i)