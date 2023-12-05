def solution(s):
    arr = list(map(int, s.split(' ')))
    return "{} {}".format(min(arr), max(arr))

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))