n, m = map(int, input().split())

dict = {}
ans = 0
for i in range(n):
    word = input()
    dict[word] = 1

for i in range(m):
    word = input()

    if word in dict:
        ans += 1

print(ans)