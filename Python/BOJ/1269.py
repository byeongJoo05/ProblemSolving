n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ad = {}
bd = {}
for i in a:
    ad[i] = 1
for i in b:
    bd[i] = 1
ans = 0
for i in ad:
    if not i in bd:
        ans += 1

for i in bd:
    if not i in ad:
        ans += 1

print(ans)