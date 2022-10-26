t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("#"+str(i+1)+" "+str(a//b)+" "+str(a%b))