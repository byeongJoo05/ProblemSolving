T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    arr.reverse()
    ans = 0
    for i in arr:
        if stack:
            if stack[-1] > i:
                ans += stack[-1] - i
            else:
                stack.pop()
                stack.append(i)
        else:
            stack.append(i)

    print("#{} {}".format(t, ans))