h, m = map(int, input().split())

sumMin = (h*60 + m)-45

if sumMin < 0:
    sumMin += 24*60

ansH = sumMin // 60
ansM = sumMin % 60

print("{0} {1}".format(ansH, ansM))