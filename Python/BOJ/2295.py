"""
x, y, z, k 는 모두 같은 집합에 속해있어야 함.
a[x] + a[y] + a[z] = a[k]
이 것을 이항하면 a[x] + a[y] = a[k] - a[z]

a[x] + a[y] 에 대한 값을 한 배열로 만들어 놓고,
a[k] - a[z] 에 대한 값을 target으로 나타내면 이분탐색으로 풀 수 있다.
"""

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr2 = []
for i in range(n):
    for j in range(i, n):
        arr2.append(arr[j] + arr[i])

arr2.sort()

result = 0
for i in range(n):
    for j in range(i, n):
        a = arr[j] - arr[i]
        start = 0
        end = len(arr2) - 1
        while start <= end:
            mid = (start + end) // 2
            b = arr2[mid]
            if a > b:
                start = mid + 1
            elif a < b:
                end = mid - 1
            else:
                result = max(result, arr[j])
                break

print(result)