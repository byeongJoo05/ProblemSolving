"""
one 이 문자열 내에 발견 됬다?
-> one을 1로 치환.

숫자 4다?
-> 그냥 냅둠

"""


def solution(s):
    answer = 0
    a = {'zero': "0", 'one': "1", 'two': "2", 'three': "3",
         'four': "4", 'five': "5", 'six': "6",
         'seven': "7", 'eight': "8", 'nine': "9"}
    for key in a.keys():
        s = s.replace(key, a.get(key)) # replace를 적용하기 위해선 치환된 배열을 원본 배열에 다시 저장해야 됨.
        print(s)
        print(key, a.get(key))

    answer = int(s)
    return answer