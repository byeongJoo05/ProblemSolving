n = int(input())
arr = set()
ans = 0
for _ in range(n):
    string = input()

    if string == "ENTER":
        arr.clear()
    else:
        if string in arr:
            continue
        else:
            arr.add(string)
            ans += 1

print(ans)