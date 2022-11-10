n = int(input())
pattern = 666
target = 0
a = 0
while True:
    if str(pattern) in str(a):
        target +=1

    if target == n:
        print(a)
        break

    a += 1