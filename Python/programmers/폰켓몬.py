from itertools import combinations

"""
1. 첫 시도 - 배열과 lambda 조합
 nums 배열에서 pick 한 만큼 순열을 돌려서 뽑아 list(key=lambda x: len(x)) 를 통해 맨 뒷 자리만 꺼내게 했다.(list[-1)
 당연히 시간초과.
 
2. 두번째 시도 - set을 통해 시간복잡도 줄이기
 아예 순열을 돌리기 전부터 데이터를 set을 통해 가공화를 하였으며, 리스트의 사용 또한 줄이기 위해 maxCount를 만들어 최대값 구하기 처럼 만들었다.
 정확성 80점이 되었지만, 히든케이스를 통과하지 못하였다.

3. 세번째 시도 - 순열도 안돌리기.
 생각해보면 순열조차 돌릴 필요도 없다. 어차피 nums 배열에서 pick 한 포켓몬의 종류의 최대는 nums를 2로 나눈 값이며, 이 것보다 작을 것이라면 중복을 줄인만큼일테니
 이 두 개의 값만 비교해서 값을 나타내면 된다.
"""
def solution(nums):
    pick = len(nums) // 2
    bigyo = len(set(nums))
    if pick > bigyo:
        pick = bigyo
    answer = pick

    """
    for i in combinations(set(nums), pick):
        # arr.append(list(set(i)))
        # print(i)
        if maxCount < len(i):
            maxCount = len(i)
    # print(maxCount)
    # arr.sort(key=lambda x: len(x))
    # print(max(len(arr[::])))
    answer = maxCount
    """
    return answer