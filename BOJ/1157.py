s = input().upper()
al = [0] * 26

for word in s:
    if ord(word) in range(65,91):
        al[ord(word)-65] += 1

if al.count(max(al)) >1: # al 중 제일 높은 수의 수를 세어줌
    print('?')
else:
    max_value = al.index(max(al))+1 # a~z 순번 # index는 요소번호 출력
    print(chr(max_value+64))