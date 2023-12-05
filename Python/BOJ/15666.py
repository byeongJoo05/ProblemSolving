n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = [0 for _ in range(10)]
start = 0
def nm(k):
    global start
    if k == m :
        for i in range(m):
            print(data[arr[i]], end=" ")
        print()
        return

    tmp = 0
    if k != 0 :
        start = arr[k-1]
    for i in range(start, n):
        if tmp != data[i]:
            arr[k] = i
            tmp = data[i]
            nm(k+1)

nm(0)