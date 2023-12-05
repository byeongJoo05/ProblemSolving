"""
n개가 수직선 위에 있는데 c개의 공유기를 설치하려함.
근데 공유기 사이의 거리를 최대 멀리해서 재고 싶음.
공유기 사이의 거리를 몇개 잴 수 있는지 확인하기
"""

n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

st, en = 1, max(arr)-min(arr)
ans = 0

while st<=en:
    mid = (st+en) // 2
    current = arr[0] # 첫번째 공유기 거리부터 구하기
    cnt = 1
    for i in arr:
        if i >= current + mid: # 공유기 위치 + 거리길이가 배열 순회한 공유기 설치 위치 비교
            current = i
            cnt += 1

    if cnt >= c: # 공유기 설치가 다 됬거나 혹은 더 많이 할 수 있음
        st = mid + 1
        ans = mid
    else: # 공유기 를 더 설치하게 해야함
        en = mid - 1

print(ans)