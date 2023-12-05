N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = arr[round(len(arr)//2)]

print(ans)