import math

while True:
    t = input()
    if int(t) == 0:
        break

    if len(t)%2 == 0: # 짝수배열
        count = 0
        for i in range(int(len(t)/2)):
            if t[i] != t[-i-1]:
                count +=1
        if count>0:
            print('no')
        else:
            print('yes')
    else:
        count = 0
        for i in range(math.floor(len(t)/2)):
            if t[i] != t[-i-1]:
                count += 1
        if count>0:
            print('no')
        else:
            print('yes')


# 남의 코드
# while True:
#     n = input()
#
#     if n == '0':
#         break
#
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')