"""
최대공약수
a와 b에 대해서(a<b) r=a%b이라고 하면, r==0이 될 때까지 b%r=r', r%r'을 했을 때 r'이 최대공약수이다.

최소공배수: (a*b)/최대공약수
"""

def solution(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]

    return answer