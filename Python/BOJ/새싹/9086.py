T = int(input())

for _ in range(T):
    ans = input()
    if len(ans) != 0:
        print(ans[0]+ans[len(ans)-1])
    else:
        print(ans[0]*2)