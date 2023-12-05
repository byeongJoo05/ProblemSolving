"""
zfill : 앞에 0을 붙일 때 사용하기 좋은 메서드.

002 만드는법
"2".zfill(3)
"""

dict = {'ADD':'0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011','OR':'0100',
                   'NOT':'0101','MULT':'0110', 'LSFTL':'0111', 'LSFTR':'1000',
                   'ASFTR':'1001','RL':'1010','RR':'1011'}

n = int(input())

for _ in range(n):
    code = input().split()
    ans = ''
    oper = code[0]
    rd = code[1]
    ra = code[2]
    rb = code[3]

    if oper[-1] == 'C':
        ans += dict.get(oper[:-1])
        ans += '1'
    else:
        ans += dict.get(oper)
        ans += '0'
    ans += '0'

    ans += str(bin(int(rd)))[2:].zfill(3)
    ans += str(bin(int(ra)))[2:].zfill(3)

    if ans[4] == '0':
        ans += str(bin(int(rb)))[2:].zfill(3)
        ans += '0'
    else:
        ans += str(bin(int(rb)))[2:].zfill(4)

    print(ans)