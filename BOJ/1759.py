"""
최소 한 개의 모음
최소 두 개의 자음
암호에서 증가하는 순서로 배열
"""

l, c = map(int, input().split())

arr = list(input().split())
arr.sort() # 알파벳 정렬
vowel = ['a', 'e', 'i', 'o', 'u'] # 모음 배열
def bt(dep, idx):
    if dep == l:
        cnt1, cnt2 = 0, 0
        for i in s: # 자음 및 모음 개수 세기
            if i in vowel:
                cnt1+=1
            else:
                cnt2+=1

        if cnt1>=1 and cnt2>=2: # 조건식에 부합하다면
            ans = "".join(s) # 문자열로 치환 후
            print(ans) # 출력
        return

    for i in range(idx, c): # 백트래킹
        s.append(arr[i]) # s배열에 문자 추가
        bt(dep+1, i+1) # 다음 문자요소 찾으러 가기
        s.pop() # 다 썼으므로 삭제


s = []
bt(0,0)