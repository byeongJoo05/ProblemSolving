import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

st, en = 0, 0
ans = int(2e9)
arr.sort()
# for st in range(n):
#     while en < n and (arr[en] - arr[st]) < m :
#         en += 1
#
#     if en == n:
#         continue
#         en = 0
#
#     ans = min(ans, arr[en]-arr[st])

while st <= en and en < n: # 시작이 끝보다 작거나 같고, 끝이 배열길이보다 작을 때 까지
    if arr[en] - arr[st] < m: # (끝 값 - 시작 값)의 값이 최저로 잡은 것보다도 작다면
        en += 1 # 오른쪽 포인터 증가
    else: # 최저 이상으로 잡혔다?
        ans = min(ans, arr[en]-arr[st]) # 일단 최소인지 판별
        st +=1 # 더 찾기 위해서 시작 요소 늘려주기

print(ans)