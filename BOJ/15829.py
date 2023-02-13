n = int(input())
Str = list(input())
ans = 0
m = 1234567891
for i in range(n):
    ans += (ord(Str[i])-96) * (31 ** i)

print(ans % m)
