"""
세 개의 수를 뽑지만 m 보단 작아야함.
브루트포스로 풀어야겠지?

"""

from itertools import combinations

n, m = map(int,input().split())

cardList = list(map(int,input().split()))

sumNum = 0

for three in combinations(cardList, 3):
    targetSum = sum(three)
    if targetSum <= m and targetSum > sumNum:
        sumNum = targetSum

print(sumNum)