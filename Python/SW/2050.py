strLine = input()

strList = list(strLine)
for i in strList:
    print(ord(i)-64, end=' ')