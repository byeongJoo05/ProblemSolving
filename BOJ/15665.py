n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = [0 for _ in range(10)]
isused = [False for _ in range(10)]

def nm(k):
    if k == m :
        for i in range(m):
            print(data[arr[i]], end=" ")
        print()
        return

    tmp = 0
    for i in range(n):
        if tmp != data[i]: # 전 데이터와 data의 i 번째와 다르다면
            arr[k] = i # 순서배열 arr의 k 공간은 i로 잡고 있기
            tmp = data[i] # tmp는 현재 i의 data배열 요소 가리키기
            nm(k+1)

nm(0)