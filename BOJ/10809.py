# 알파벳 찾기

S = input()

#아스키 코드 a = 97, z= 122 , 반드시 써먹게 암기

for i in range(97, 123): #range(시작, 원하는 끝+1)
    if chr(i) in S:
        print(S.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')