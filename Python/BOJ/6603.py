k = 1

def bt(p, arr, idx): # 배열 깊이, 원본 배열, 현재 찾는 배열 요소
    if p == 6: # 깊이가 원하는 6까지 왔다면
        print(* l) # 출력하고나서
        return # 함수 끝내기

    for i in range(idx, k): # 오름차순으로 뽑기 위한 반복문. 범위를 통해 잘라서 찾을 수 있음
        l.append(arr[i]) # l에 사용
        bt(p+1, arr, i+1) # 깊이와 찾을 요소 +1 씩 해주기
        l.pop() # 사용이 끝난 후 pop 해주기

while k != 0 :
    arr = list(map(int, input().split()))
    k, arr = arr[0], arr[1:]
    arr.sort()
    l = []
    bt(0, arr, 0)
    print()