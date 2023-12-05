n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = [0 for _ in range(10)]

def nm(k):
    global start
    if m == k :
        for i in range(m):
            print(data[arr[i]], end=" ")
        print()
        return


    for i in range(n):
        arr[k] = i
        nm(k+1)


nm(0)