str = input()

answer = ''

for alpha in str:
    if alpha.isupper():
        answer+=alpha.lower()
    else:
        answer+=alpha.upper()
        
print(answer)