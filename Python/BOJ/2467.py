"""
이분탐색이나 투포인터로 풀어야 하는 문제.

왜 이분탐색으로 풀어야 됬을까?
1. 두 용액을 섞어서 만드는 것이기에 일단 두 개의 요소를 추출해서 해야함
2. 가장 0 에 가깝게끔 만드는 것이기에, 파라메트릭 서칭에 관련된 향기가 강하게 남

다른 풀이과정 참고를 해보니
일단 한 용액은 순차적으로 뽑아주고, 다른 용액을 이분탐색을 통해
0과 가장 가깝게 만들어보게 풀어야함.
"""

n = int(input())
arr = list(map(int, input().split()))
minVal = int(3e9)
ansl, ansr = 0, 0
for i in range(n-1):
    current = arr[i]
    st = i+1 # current 용액보다 1개 더 높은 곳부터 찾기
    en = n-1

    while st <= en:
        mid = (st+en) // 2
        com = current + arr[mid] # 최소 비교를 위한 용액의 합

        if abs(com) < minVal:
            minVal = abs(com)
            ansl = i
            ansr = mid

            if com == 0: # 두 용액의 합이 0 이면 완벽한 최적값이므로 break
                break

        if com < 0: # 음수라면 양수를 더해야 0에 가까워지므로 스타트지점을 양수쪽으로 옮긴다.
            st = mid + 1
        else: # 양수라면 음수를 더해야 0에 가까워지므로 엔드지점을 음수쪽으로 옮긴다.
            en = mid - 1

print(arr[ansl], arr[ansr])