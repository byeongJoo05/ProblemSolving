n = int(input())
dict = {}

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        dict[name] = state
    else:
        del dict[name]

dict = sorted(dict, reverse=True)
for name in dict:
    print(name)