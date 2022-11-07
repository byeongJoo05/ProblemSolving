num = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

a = int(input())
b = int(input())
c = int(input())
sum = a * b * c

for i in str(sum):
    if i in num:
        num[i] += 1

for i in num.values():
    print(i)
