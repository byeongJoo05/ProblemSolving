"""
1. a(i) + a(j) = x
2. a(i) 항을 뺀 a(j)의 합산이 x와 같다면 가능함
3. 그러면 어떻게 x-i = j 란 것을 만들 수 있을 것인가??
4. a[i] + a[x-i] = x
5. 무조건 x 만큼 0을 만들면 되겠네?
"""

"""
배열로 풀려고 했지만 계속 런타임 에러가 뜸. for문도 줄일 만큼 줄였는데도 뜨는 이유가 무엇인지......
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
scoreList = [0] * x
count = 0
for i in arr:
    scoreList[i] += 1

for i in range(1, int(x/2)):
    if scoreList[i] == 1 and scoreList[x-i] == 1:
        count += 1

print(count)
"""

"""
투포인터로 풀어보기
"""

n = int(input()) # 데이터의 개수
arr = list(map(int, input().split())) # 데이터들
x = int(input()) # 찾고자 하는 부분합
arr.sort() #데이터를 정렬하고 사용하기
start, end = 0, n-1 # 시작 요소와 끝 요소 잡아 놓기. arr 배열에서 사용할 것임
count = 0

while start < end: #start가 끝 요소까지 왔다면
    tmp = arr[start] + arr[end] # 합산계산
    if tmp == x: count += 1
    if tmp < x:
        start +=1
        continue
    end -= 1 # 누적합이 타겟보다 크다면 end를 줄여주기.
print(count)