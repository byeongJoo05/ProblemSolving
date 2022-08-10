n = int(input())
user = list(map(int, input().split()))
user.sort()

count = 0 # 그룹에 참여할 수 있는 인원수
result = 0 # 그룹 갯수

for i in user:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)