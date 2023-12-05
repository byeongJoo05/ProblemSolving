import sys

input=sys.stdin.readline

thr = []

thr = list(range(1,31))

for _ in range(28):
    stu = int(input())
    thr.remove(stu)

thr.sort()

print(min(thr))
print(max(thr))