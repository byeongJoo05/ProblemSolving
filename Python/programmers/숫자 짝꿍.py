"""
set(X) & set(Y) 를 통하여 2중 for문을 사용하지 않고도 변수값 판별이 가능했다.

count() 메서드를 활용하자.

count(param) 을 통하여 List 내 param 값의 갯수를 셀 수 있다.
"""

def solution(X, Y):
    answer = ''
    l = []
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            l.append(i)

    l.sort(reverse=True)

    if not l:
        return "-1"
    if l[0] == '0':
        return "0"

    answer = "".join(l)
    return answer