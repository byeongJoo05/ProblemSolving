"""

"""

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = [0 for _ in range(10)]
isused = [False for _ in range(10)]
def nm(k, st):

    if m == k :
        for i in range(m):
            print(data[arr[i]], end=" ")
        print()
        return

    check = 0
    for i in range(st, n):
        if not isused[i] and data[i] != check:
            isused[i] = True
            arr[k] = i
            check = data[arr[k]]
            nm(k+1, i+1)
            isused[i] = False


nm(0, 0)