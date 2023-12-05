n = 1260 #돈
count = 0 #개수

coin_types=[500,100,50,10]

for coin in coin_types :
    count += n // coin # 먼저 500원 어치만큼 나눔. 그 이후 100원 어치만큼 .... 10원 어치만큼...
    n %= coin # 260 -> 60 -> 0

print(count)