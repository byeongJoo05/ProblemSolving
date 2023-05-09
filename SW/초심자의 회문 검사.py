T = int(input())

for t in range(1, T+1):
    arr = list(input())

    if arr == arr[::-1]:
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))