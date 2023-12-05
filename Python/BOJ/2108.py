from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
print(round(sum(arr)/n))
print(arr[int(len(arr)/2)])

arrC = Counter(arr).most_common()
if len(arrC) > 1:
    if arrC[0][1] == arrC[1][1]:
        print(arrC[1][0])
    else:
        print(arrC[0][0])
else :
    print(arrC[0][0])

print(arr[-1] - arr[0])