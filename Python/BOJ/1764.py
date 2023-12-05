n, m = map(int, input().split())
dict = {}
arr = []
for _ in range(n):
    dict[input()] = 1

for _ in range(m):
    target = input()
    if target in dict:
        arr.append(target)

print(len(arr))
arr.sort()
for i in arr:
    print(i)