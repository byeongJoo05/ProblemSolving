n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = [0 for _ in range(10)]
start = 0
def nm(k):
    global start
    if m == k :
        for i in range(m):
            print(data[arr[i]], end=" ")
        print()
        return

    if k != 0 :
        start = arr[k-1] + 1
    for i in range(start, n):
        arr[k] = i
        nm(k+1)


nm(0)