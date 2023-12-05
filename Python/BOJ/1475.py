"""
한 세트는 숫자 0~9 만 하나씩 가능함.
근데 6은 9로 뒤집을 수 있음
9999662 같은 경우는 3이 나와야 함.
"""

n = input()
numList = [0,0,0,0,0,0,0,0,0,0]
for i in n:
    if i =="9":
        numList[6] += 1
    else:
        numList[int(i)]+=1
if numList[6] % 2 == 0:
    numList[6] //= 2
else:
    numList[6] //= 2
    numList[6] +=1

print(max(numList))