"""
가능한 한 최대의 => 파라메트릭 서칭
지금까지는 요소값으로만 찾았는데 값으로도 찾을 수 있음
"""
n = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

st, en = 0, max(arr)
ans = 0

while st <=en:
    mid = (st+en) //2
    cmp = 0
    for i in arr: # 지방예산요청을 순회하면서
        if i > mid: # 지방예산요청보다 많이 줄 수 있다면
            cmp += mid # 평균 상한액을 주고
        else: # 평균 상한액 보다 더 많이 요청했다면
            cmp += i # 그 금액을 준다.

    if cmp <= target: # 더한 총액이 타겟보다 작다면
        st = mid +1 # 평균치보다 높게 st를 잡아본다
    else: # 그게 아니라면
        en = mid - 1 # 평균치보다 en포인트를 내려본다

print(en)