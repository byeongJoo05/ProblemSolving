"""
1. w : 가로 길이, h : 세로 길이
2. 만약 카드를 회전시켜서 넣어질 수 있다면 그 것 또한 최소로 모든 조건에 일치하는 것이 됨.
"""

def solution(sizes):
    answer = 0
    wArr = []
    hArr = []

    for w, h in sizes:
        if w < h: # 가로, 세로 바꾸면 둘 다 맥스로 잡을 수 있을듯
            w, h = h, w
        wArr.append(w)
        hArr.append(h)

    answer = max(wArr) * max(hArr)
    return answer