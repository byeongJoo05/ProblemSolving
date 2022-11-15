"""
occurs <-> succor 가 애너그램
o c c u r s

dared <-> bread 는 애너그램이 아님.
d a r e d
b r e a d
a:2, b:1, d:3, r: 2, e: 2
둘이 애너그램이 되려면 dared는 d가 없어야 하며, bread는 b 가 없어야 함.

ared <-> read 는 애너그램
a r e d
a:2, r:2, e:2, d:2
문자마다 카운트를 어디에 정리해 놓아야 한다고 생각함.
두 개의 문자열을 카운트에 같이 넣어놓고, 만일 문자열의 카운트가 홀 수일 경우 애너그램 성립이 불가함.


"""
from collections import Counter
a = input()
aCounter = Counter(a)
b = input()
bCounter = Counter(b)

print(sum((aCounter-bCounter).values()) + sum((bCounter-aCounter).values()))