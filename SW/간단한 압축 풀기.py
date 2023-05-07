T = int(input())

for t in range(1,T+1):
    n = int(input())
    print("#{}".format(t))
    arr = ""
    cnt = 0
    arr = []
    for _ in range(n):
        ch, num = input().split()
        num = int(num)
        while num > 0 :
            arr.append(ch)
            num -= 1
            cnt += 1

            if cnt == 10:
                print("".join(arr))
                cnt = 0
                arr = []

    if arr:
        print("".join(arr))
        arr=[]