n, m = map(int, input().split())

isused = [False for _ in range(10)]
arr = [0 for _ in range(10)]
start = 1

def nm(k):
    global start
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    if k != 0:
        start = arr[k-1]

    for i in range(start, n+1):
        isused[k] = True
        arr[k] = i
        nm(k+1)
        isused[k] = False

nm(0)