"""
현재 위치 - 같은 문자 위치 = 표현할 수 있는 위치 차이
현재 위치 - 같은 문자 위치 = 0 -> 앞에 아무고토 없다는 뜻으로 -1을 리턴해주어야 함.
"""

"""
딕셔너리를 이용하는 게 답이였다.

dict = {} <- 요런 모습으로 선언을 해주면 된다.
딕셔너리는 key-value 형태로 사용하면 되는데 이 문제에선 key는 문자를, value는 index를 넣어주어 사용하였다.

또한 enumerate를 사용하여 idx와 문자를 지정하게 했다. 순차적 접근을 하는데 꺼내올 값의 번호를 같이 반환해준다. 이건 공부 좀 하면 실용적일 수 있을 것이라고 본다.
"""

def solution(s):
    answer = []
    arr = list(s)
    dict = {}

    for idx, word in enumerate(arr):
        if word not in dict:
            answer.append(-1)
            dict[word] = idx
        else:
            now = idx - dict[word]
            answer.append(now)
            dict[word] = idx
    """
    for i in range(len(arr)): # 현재 문자열 내 index 찾기
        if i == arr.index(arr[i]):
            answer.append(-1)
        else:
            # 인접한 위치의 인덱스 번호를 알아와야함.
            # 이분탐색인가? 문자열 이분탐색이 말이 됨?
            # 딕셔너리? 딕셔너리 key를 숫자로 두어서 이분탐색을 한다면 가능할지도?
            idx = i - arr.index(arr[i])
            answer.append(idx)
    """
    print(dict)
    return answer