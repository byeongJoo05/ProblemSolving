"""
초기값 = 1 - L


"""
from collections import deque

n, m = map(int, input().split())
d = list(map(int, input().split()))
dq = deque()

for i in d:
