def solution(n, m, section):
    answer = 0
    painted = 0

    for sec in section:
        if sec > painted:
            painted = sec + m - 1  # 추 후 페인트할 곳은 색칠하고 난 이후부터
            answer += 1
    return answer