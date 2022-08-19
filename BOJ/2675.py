t = int(input())

for _ in range(t):
    r, s = input().split()
    for a in s:
        print(a*int(r), end='')
    print()