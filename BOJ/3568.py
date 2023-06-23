data = list(input().split())
vartype = data[0]
addplus = ['*','[',']','&']
for i in range(1, len(data)):
    add = ''
    char = ''
    ans = ''
    for c in data[i]:
        if c in addplus:
            add+=c
        if c.isalpha():
            char+=c
    reform = ''
    for j in list(add)[::-1]:
        if j == ']':
            reform += '[]'
        elif j == '[':
            continue
        else:
            reform += j
    ans += (vartype+reform+' '+char+';')
    print(ans)