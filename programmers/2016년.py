def solution(a, b):
    # 1 금, 2 토, 3 일, 4 월, 5 화, 6 수, 7 목
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    # 1월부터 ~ 12월
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = -1

    for i in range(a - 1):
        date += month[i]

    answer = day[(date + b) % 7]
    return answer