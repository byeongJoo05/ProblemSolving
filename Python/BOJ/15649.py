n, m = map(int, input().split())

arr = [0 for _ in range(10)] # 출력할 데이터 리스트
isused = [False for _ in range(10)] # 사용했는지 확인할 불린 리스트

def nm(k) :
    if k == m :
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, n+1):
        if not isused[i]: # i의 상태가 사용되지 않았다면
            arr[k] = i # k번째 요소는 i를 이용
            isused[i] = True # 상태가 사용됬음을 보여줌
            nm(k+1) # 그 다음 요소 찾기
            isused[i] = False # i의 상태를 다 사용했으므로 False로 닫아주기

nm(0)