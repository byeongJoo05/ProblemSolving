"""
키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표

1. 백스페이스 경우
' - ' 가 주어짐.
커서의 바로 앞에 글자가 존재하면 글자 지워주기.

2. 화살표의 경우
' < ' 와 ' > ' 가 주어짐
'<' '>'으로 왼쪽, 오른쪽 1씩 움직임.
"""

n = int(input())

for _ in range(n):
    test = input()
    left = []
    right = []

    for i in test:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    print("".join(left)+"".join(reversed(right)))
# n = int(input())

# for _ in range(n):
#     test = list(input())
#     ans = []
#     cur = 0
#     for i in test[0:]:
#         print(test[0:])
#         print(i)
#         if i == "<":
#             # print(cur)
#             if cur != 0:
#                 cur -= 1
#         elif i == ">":
#             if cur != len(test)-1:
#                 cur += 1
#         elif i == "-":
#             if cur < 1:
#                 test.pop(cur)
#             else:
#                 test.pop(cur)
#                 cur -= 1
#                 test.pop(cur)
#         else:
#             # print(i)
#             # print("알파벳만 : "+ str(cur))
#             ans.append(test[cur])
#             cur+=1
#
#     print(str(ans))