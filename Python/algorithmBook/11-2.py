s = input()
result = int(s[0])

for i in range(1,len(s)):
    data = int(s[i])
    if data <= 1 or result <=1:
        result += data
    else:
        result *= data

print(result)