def solution(s):
    answer = 0
    cnt = 0  # 처음 문자의 갯수
    cmp = 0  # 비교할 문자의 갯수 합
    for i in range(len(s)):
        if cnt == cmp:
            answer += 1
            cur = s[i]
            cnt = 0
            cmp = 0

        if s[i] == cur:
            cnt += 1
        else:
            cmp += 1

        print(cnt, cmp)
    return answer