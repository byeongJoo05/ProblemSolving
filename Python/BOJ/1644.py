"""
에라토스테네스의 체 + 투포인터가 합쳐진 문제
소수의 합을 통해 n을 구할 수 있게 해야함

소수부터 구해보자 - 에라토스테네스
"""

def prime():
    for i in range(2,n+1):
        if isprime[i]:
            arr.append(i)
        for j in range(2*i, n+1, i):
            isprime[j] = 0

n = int(input())
isprime = [0, 0] + [1 for _ in range(n-1)]
arr = [] # n까지의 범위에서 소수만을 저장할 arr
prime()
st, en = 0, 0
ans = 0
while en <= len(arr):
    cmp = sum(arr[st:en])
    if cmp == n:
        ans += 1
        en += 1
    elif cmp < n:
        en += 1
    elif cmp > n:
        st +=1

print(ans)