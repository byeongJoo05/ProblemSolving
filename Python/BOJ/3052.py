namoji = []

for _ in range(10):
    a = int(input())
    b = a % 42
    namoji.append(b)

ans = set(namoji)
print(len(ans))