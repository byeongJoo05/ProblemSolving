"""
1. 현재가 O이면 카운트를 1씩 증가시키고, sum에 카운트 더하기
2. 만약 현재가 X가 되면, 카운트는 다시 0으로 만들기
"""

t = int(input())

for _ in range(t):
    line = input()

    count = 0
    sum = 0
    for ch in line:
        if ch =='O':
            count +=1
            sum += count
        else:
            count = 0
    print(sum)