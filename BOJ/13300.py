n, k = map(int, input().split())
wList = [0] * 1000
mList = [0] * 1000

for j in range(n):
    s, y = map(int, input().split())
    # 학년별 인원수 체크
    if s == 0:  # 여자
        wList[y] += 1
    else:  # 남자
        mList[y] += 1

for j in range(1, 7):
    if wList[j] % k == 0:
        wList[j] = wList[j] // k
    else:
        wList[j] = (wList[j] // k) + 1

    if mList[j] % k == 0:
        mList[j] = mList[j] // k
    else:
        mList[j] = (mList[j] // k) + 1

print(sum(wList) + sum(mList))