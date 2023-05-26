conarr = []

for num in range(1,10001):
    for i in str(num):
        num += int(i) # 무조건 생성자가 있음
    conarr.append(num)

conarr = set(conarr) # 중복 수 줄이기
for i in range(1, 10001):
    if not i in conarr: # 중복이 아니라면 프린트
        print(i)