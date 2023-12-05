"""
v의 높이를 가진 나무를 X 번 타게 되면
v = X*a - X*b
인데 낮에 도달할 수 있으니 밤에 미끄러질 것을 -1 해줘야됨.
따라서, v = X*a - (X-1)*b.
X의 값으로 치환하면, v = X*(a-b)+b -> X = (v-b)/(a-b)
"""

import sys, math

input = sys.stdin.readline

a, b, v = map(int, input().split())
X = (v-b)/(a-b)
print(math.ceil(X)) # 올림