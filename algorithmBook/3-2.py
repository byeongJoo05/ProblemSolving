# N, M, K
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

result = 0
data.sort()
first = data[n-1]
second = data[n-2]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1 # m 감소시켜주기

    if m == 0:
        break
    result += second
    m -= 1

print ( result)

