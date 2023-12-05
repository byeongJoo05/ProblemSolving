"""
orders 에 주문한 음식의 양이 5개이고 5 코스짜리여도, 손님이 한 번 밖에 주문을 안했다면 뽑아주면 안됨
"""

from itertools import combinations


def solution(orders, course):
    dict = {}  # 딕셔너리 선언
    answer = []  # 정답을 담는 리스트

    for order in orders:  # 문자열리스트에서 문자열 한 개 씩 꺼내기
        food = list(order)  # 문자열을 문자로 만들어주기
        food.sort()  # 문자 알파벳순 정렬

        for i in course:  # 코스만큼 길이가 필요함
            for j in combinations(food, i):  # 코스의 길이만큼 문자리스트에서 조합이 된 문자열 뽑기
                key = ''.join(j)  # 키로 만들기

                if key in dict:  # 만약 키가 딕셔너리에 등록이 되어 있다면?
                    dict[key] += 1  # 그 키는 이미 존재했던 것이니 +1 추가
                else:  # 존재한 게 아니라면
                    dict[key] = 1  # 1 넣어주기

    for i in course:  # 또 다시 코스의 길이만큼 돌아야될 반복문을 만들기
        l = []
        for j in dict.keys():  # 딕셔너리 내 key 값을 꺼내와서 for문으로 돌린다
            if len(j) != i or dict[j] == 1:  # 만약 key의 길이가 코스와 같지 않거나 key의 value가 1이면
                continue  # 뛰어 넘는다
            l.append((j, dict[j]))  # 그게 아니라면 조건에 충족된 것이니 리스트에 추가(key, value 저장)
        l.sort(key=lambda x: x[1])  # 람다를 이용해 value를 오름차순으로 정렬
        if not l:  # 만약 l 리스트가 비어있다면
            continue  # 건너 뛴다
        k, maxV = l.pop()  # max값과 같은 값을 찾기 위해 가장 큰 수
        answer.append(k)  # 일단 max 값이 였으니 정답에 집어넣기
        while True:  # 이제 max값과 같은 value를 더 찾아보기
            if not l:  # 만약 l 이 비어있다면
                break  # 찾을 수도 없으니 while문 탈출
            tmpK, tmpV = l.pop()
            if maxV == tmpV:  # tmpV 와 위에서 잡은 maxV가 같으면 최대값 중복이니
                answer.append(tmpK)  # answer에 추가
            else:  # 없으면 고유한 최대값이므로
                break  # 반복문 탈출

    answer.sort()  # 문자열 정렬

    return answer