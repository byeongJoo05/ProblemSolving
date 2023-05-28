n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

dict = {}
ans=[]

for i in arr:
    dict[i] = 0

for i in target:
    if i in dict:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)