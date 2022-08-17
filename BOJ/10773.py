stack =[]
ans=0
k = int(input())

for i in range(k):
    data = int(input())
    if data > 0 :
        stack.append(data)
    else:
        stack.pop()

for i in stack:
    ans += i

print(ans)