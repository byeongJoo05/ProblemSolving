"""
매개변수탐색(파라메트릭 서칭) 공부
- 최대값, 최적값 찾을 때 사용하는 알고리즘 기법

템플릿 자체는 이분탐색과 비슷한 느낌으로 흘러가는 것 같음.

다른 점
시작과 끝은 요소값이기에 0과 배열의 끝자락 가져가기

1. 파라메트릭 서칭
중간값이 0에 도달하면 같은 길이에 막대과자를 나눠질 수 없다는 것을 의미함

mid 는 과자의 길이가 되는 것이다.

각 과자를 mid로 나누었을 때 개수를 세면 되며,
개수가 나눠먹을 수 있는 만큼(m)보다 크거가 같으면 ans에 적합하다.
그 중 가장 큰 ans를 뽑으면 된다.
"""
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

st, en = 0, int(1e9)

while st <= en :
    total = 0
    mid = (st+en) // 2

    if mid == 0:
        ans = 0
        break

    for i in arr:
        if i >= mid:
            total += (i // mid)

    if total >= m:
        ans = mid
        st = mid + 1
    else:
        en = mid - 1

print(ans)