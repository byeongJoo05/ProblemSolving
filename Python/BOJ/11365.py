memo = []

while True:
    text = input()
    if text == "END":
        break
    memo.append(text)

for i in memo:
    ans = ""
    for a in i[::-1]:
        ans += a
    print(ans)