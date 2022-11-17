import sys
input= sys.stdin.readline

n = int(input())

people = []

for _ in range(n):
    age, name = input().split()
    people.append([age, name])

people.sort(key= lambda x : int(x[0]))

for i , j in people:
    print(i, j)