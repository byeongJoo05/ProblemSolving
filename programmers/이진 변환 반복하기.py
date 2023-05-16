"""
1. 0에 대한 저장을 해야될 변수, 몇 번 이진 치환을 했는지 찾아야될 변수 필요
2. 1에 대한 값만 뽑아서 어떤 리스트에 저장 후 길이에 대해 2진 치환하면 되지 않을까?
"""

def solution(s):
    answer = []

    cnt_binary = 0

    cnt_zero = 0

    while True:
        if s == "1":
            break
        cnt_binary += 1
        cnt_zero += s.count("0")

        s = s.replace("0", "")

        len_s = len(s)

        s = bin(len_s)[2:]

    answer.append(cnt_binary)
    answer.append(cnt_zero)

    return answer