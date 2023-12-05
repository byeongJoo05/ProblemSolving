n, m = map(int, input().split())
isused = [False for _ in range(10)]
arr = [0 for _ in range(10)]
start = 1 # 상태 변화가 일어날 때 수열을 오름차순으로 만들어 줄 변수

def nm(k):
    global start
    if m == k:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    if k != 0 : # 상태 공간이 0이 아니라면
        start = arr[k-1] + 1 # 다음 수열부터는 전 상태공간의 값보다 1을 높여 사용해야한다.

    for i in range(start, n+1):
        if not isused[i]:
            isused[k] = True
            arr[k] = i
            nm(k+1)
            isused[k] = False

nm(0)