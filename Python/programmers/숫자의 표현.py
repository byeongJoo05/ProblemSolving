"""
투포인터 문제

왜? 부분합 문제이지만, 연속된 숫자 배열을 나타내고 있으며 좌측 우측이 계속 이어가지고 않고, 시작점 끝점이 애매하니까

1. 일단 n까지의 숫자를 1부터 n 까지 배열에 숫자 하나하나씩 집어넣기
2. left를 0~14 , right를 증가하는 식으로 한다.
3. 만약 n을 찾았다면 left쪽을 줄여 나간다.
4. 근데 r까지의 합이 sum보다 작아졌다면 -> 다시 r 길이를 늘려 더해보기.
"""


def solution(n):
    r = 0
    result = 0
    arr = []
    sum = 0

    for i in range(1, n + 1):
        arr.append(i)

    for l in range(len(arr)):

        while sum < n and r < n:
            sum += arr[r]
            r += 1
        if sum == n:
            result += 1

        sum -= arr[l]

    return result