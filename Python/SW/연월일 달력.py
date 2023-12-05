T = int(input())

for t in range(1, T+1):
    flag = True
    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30 ,31]

    n = input()
    year = n[:4]
    mon = n[4:6]
    day = n[6:]

    # if year[0] == '0':
    #     print("#{} -1".format(t))
    #     continue

    if int(mon) < 1 or int(mon) >12 :
        print("#{} -1".format(t))
        continue

    if int(day) < 1 or arr[int(mon)-1] < int(day):
        print("#{} -1".format(t))
        continue

    print("#{} {}/{}/{}".format(t, year, mon, day))