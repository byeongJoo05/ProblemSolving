import sys

n, m = map(int, input().split())
dict = {}
cnt = 0
for i in range(m):
    dict[sys.stdin.readline().strip()] = i

dict = sorted(dict.items(), key=lambda x:x[1])

for k, v in dict:
    if cnt == n:
        break
    print(k)
    cnt+=1