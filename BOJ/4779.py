def cut(a,n): # a = 시작점
    if n == 1:
        return
    for i in range(a + n//3, a +(n//3)*2): # 가운데 문자열을 공백으로
        result[i] = ' '
    cut(a, n//3) # 왼쪽 잘라나가기
    cut(a + n//3 * 2, n//3) # 오른족 잘라나가기
import sys
while True:
    try :
        N = int(sys.stdin.readline())
        result = ['-']*(3**N) # 최초 리스트 집합
        cut(0,3**N) # 자르기
        print(''.join(result))
    except : # EOF 발생시
        break # 종료

# import sys
# def recur(offset, i , data):
#     offset = offset // 3
#     if offset == 0:
#         return
#
#
#     for j in range(i+offset, i+offset*2):
#         data[j] = ' '
#     recur(offset, i, data)
#     recur(offset, i+offset*2, data)
#
# while True:
#     try:
#         n = int(sys.stdin.readline())
#         data = ['-' for _ in range(pow(3,n))]
#         recur(pow(3,n), 0, data)
#         answer = ''
#         for i in data:
#             answer += i
#         print(answer)
#     except EOFError:
#         break