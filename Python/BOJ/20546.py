money = int(input())

jugalist = list(map(int, input().split()))

# 준현이 초기 자본, 성민이 초기 자본
junMoney, sungMoney = money, money

# 준현이 주가, 성민이 주가
junjuga, sungjuga = 0, 0

for i in range(len(jugalist)):
    juga = jugalist[i]

    # 준현이 전략
    if junMoney != 0 and (junMoney - juga) >= 0:
        junjuga += (junMoney//juga)
        junMoney %= juga

    # 성민이 전략
    if i > 2:
        if jugalist[i-3] > jugalist[i-2] > jugalist[i-1]:
            sungjuga += (sungMoney//juga)
            sungMoney %= juga

        elif jugalist[i-3] < jugalist[i-2] < jugalist[i-1]:
            sungMoney += sungjuga*juga
            sungjuga = 0

jun = junMoney + (junjuga*jugalist[-1])
sung = sungMoney + (sungjuga*jugalist[-1])
if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")