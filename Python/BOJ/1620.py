"""
isdigit() 으로 자료형 판별 가능. 까먹지 말자

dict 에서 힘들게 key, value를 꺼내지 말고 dict[key] = value, dict[value] = key를 통해
조금 더 쉽게 값을 꺼내올 수 있도록 하는 방식도 있다.
"""
import sys

n, m = map(int, input().split())
dict = {}
for i in range(1, n+1):
    word = sys.stdin.readline().strip()
    dict[word] = i
    dict[i] = word

for i in range(m):
    word = sys.stdin.readline().strip()

    if word.isdigit():
        print(dict[int(word)])
    else:
        print(dict[word])