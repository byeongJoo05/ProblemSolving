n,m = map(int, input().split())
arr = [0 for _ in range(10)]

def nm(k):
    if m == k:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, n+1):
        arr[k] = i
        nm(k+1)

nm(0)