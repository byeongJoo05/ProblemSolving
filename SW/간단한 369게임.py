N = int(input())

arr = []

for i in range(1,N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        l = 0
        for k in str(i):
            if k == "3" or k == "6" or k == "9":
                l +=1
        arr.append("-" * l)
    else:
        arr.append(str(i))

print(* arr)