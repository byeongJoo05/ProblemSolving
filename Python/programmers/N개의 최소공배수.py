def lcm(a, b):
    A, B = a, b
    while b > 0:
        a, b = b, a % b

    GCD = a
    return A * B // GCD


def solution(arr):
    arr.sort()
    answer = arr[0]

    for i in range(len(arr) - 1):
        answer = lcm(answer, arr[i + 1])
    return answer