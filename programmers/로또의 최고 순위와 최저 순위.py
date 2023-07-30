def rank(i, answer):
    if i == 6:
        answer.append(1)
    elif i == 5:
        answer.append(2)
    elif i == 4:
        answer.append(3)
    elif i == 3:
        answer.append(4)
    elif i == 2:
        answer.append(5)
    else:
        answer.append(6)

    return


def solution(lottos, win_nums):
    answer = []
    win = 0
    lose = 0
    for num in lottos:
        if num == 0:
            win += 1
            continue
        if num in win_nums:
            win += 1
            lose += 1

    rank(win, answer)
    rank(lose, answer)

    return answer