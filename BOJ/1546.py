n = int(input())
scoreList = list(map(int, input().split()))
bestScore = max(scoreList)
for i in range(n):
    scoreList[i] = scoreList[i]/bestScore*100

avr = sum(scoreList)/n
print(avr)