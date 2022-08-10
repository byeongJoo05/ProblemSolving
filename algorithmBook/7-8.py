n, m = map(int, input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start+end) //2
    for data in array:
        if data > mid:
            total += data- mid # 잘린만큼 합산
    if total < m: # 합산해도 요청한 길이보다 되지 않으면
        end = mid -1 # 더 잘라주기
    else:
        result = mid
        start = mid +1


print(result)