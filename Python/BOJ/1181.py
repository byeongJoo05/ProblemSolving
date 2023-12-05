import sys

input = sys.stdin.readline

n = int(input())

word = []

for _ in range(n):
    word.append(input().strip())
set_word = list(set(word))

set_word.sort() # 알파벳 순
set_word.sort(key=len) # 길이순
for ans in set_word:
    print(ans)