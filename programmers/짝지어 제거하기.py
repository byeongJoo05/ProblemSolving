"""
스택인 아닌 투포인터라고 생각한 문제.

왜 스택이였을까?
1. 한쪽에서만 검사를 해줘도 가능한 문제였음.
2. 스택에 top을 사용함으로써 만약 문자열 탐색 중 i 와 top이 일치한다면 지우기만 하면 됨.
3. 만약 stack이 쌓여있다면 문자열 짝짓지 못했다는 것과 같다는 것이므로 answer은 언제나 0을 나타내면 됨.
"""


def solution(s):
    answer = 0
    stack = []

    for i in s:
        if not stack:
            stack.append(i)
        elif stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print(stack)
    if not stack:
        answer = 1

    return answer