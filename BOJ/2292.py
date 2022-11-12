n = int(input())
cur = 1
ans = 1
six_count = 6

while n > cur:
    ans +=1
    cur += six_count
    six_count += 6
print(ans)