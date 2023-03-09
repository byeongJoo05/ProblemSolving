"""
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 return

람다식으로 x[-1], x[0]을 했을 경우 70점을 맞고 런타임 에러가 나오게 됨.
정렬을 맥스힙으로 해서 정렬을 하는게 낫지 않을까 생각함.
"""
import heapq


def solution(N, stages):
    answer = []
    h = []
    for i in range(1, N + 1):
        nowStep = 0
        allStep = 0
        val = 0
        for j in stages:
            if j >= i:
                allStep += 1

            if i == j:
                nowStep += 1

        if allStep != 0: # 분모가 0이면 런타임 에러 발생함
            val = nowStep / allStep
        # answer.append((i, nowStep/allStep))
        heapq.heappush(h, (-(val), i))
        # print(h)

    for i in range(len(h)):
        answer.append(heapq.heappop(h)[1])
    # answer.sort(key=lambda x: (-x[1],x[0]))
    # ans = []
    # for idx, val in answer:
    #     ans.append(idx)
    return answer