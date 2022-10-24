T = int(input())
calList = []

for _ in range(T):
    calList.append(input())

MON = ['01','02','03','04','05','06','07','08','09','10','11','12']
DAY31 = ['01','03','05','07','08','10','12']
DAY30 = ['04','06','09','11']
DAY28 = ['02']
for num in range(T):
    if str(calList[num][4:6]) not in MON:
        print("#"+str(num+1)+" -1")
        continue
    if calList[num][4:6] in DAY31:
        if int(calList[num][6:]) in range(1,32):
            print("#"+str(num+1)+" "+str(calList[num][:4])+"/"+str(calList[num][4:6])+"/"+str(calList[num][6:]))
        else:
            print("#"+str(num+1)+" -1")
    elif calList[num][4:6] in DAY30:
        if int(calList[num][6:]) in range(1,31):
            print("#"+str(num+1)+" "+str(calList[num][:4])+"/"+str(calList[num][4:6])+"/"+str(calList[num][6:]))
        else:
            print("#"+str(num+1)+" -1")
    elif calList[num][4:6] in DAY28:
        if int(calList[num][6:]) in range(1,29):
            print("#"+str(num+1)+" "+str(calList[num][:4])+"/"+str(calList[num][4:6])+"/"+str(calList[num][6:]))
        else:
            print("#"+str(num+1)+" -1")