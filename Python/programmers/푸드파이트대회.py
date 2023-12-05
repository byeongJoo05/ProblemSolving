from collections import deque
"""
데크에 index를 붙여 사용하니 list가 [1,3,2,3] 일 경우, 1도 3개고 3도 3개이다보니 index가 순차적 접근을 할 때, 1만 찾아주는 문제가 발생하게 되었다.
그리해서 index의 번호를 직접 만들어주어 food[i]의 값을 찾아주는 형태로 바꾸어서 사용했다.
"""
def solution(food):
    answer = ''
    dq = deque()
    dq.append(0)
    for i in range(len(food)-1,0,-1): #index 의 번호를 출력하기
        if food[i] % 2 == 0: # i가 짝수라면
            for _ in range(food[i]//2):
                dq.append(i)
                dq.appendleft(i)
        else:
            j = food[i] - 1
            for _ in range(j//2):
                dq.append(i)
                dq.appendleft(i)
    for i in list(dq):
        answer += str(i)
    return answer