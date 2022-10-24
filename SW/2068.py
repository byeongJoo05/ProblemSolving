T = int(input())
numList = []
for i in range(T):
    numList.append(map(int,input().split()))
    a = max(numList[i])
    print("#"+str(i+1)+" "+str(a))
