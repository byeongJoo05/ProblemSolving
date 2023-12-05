def solution(keymap, targets):
    answer = []
    dict = {}
    for key in keymap:
        l = list(key)
        for i in l:
            if not i in dict:
                dict[i] = l.index(i) + 1
            else:
                if dict[i] > l.index(i) + 1:
                    dict[i] = l.index(i) + 1

    for target in targets:
        cnt = 0
        flag = True
        for i in target:
            if not i in dict:
                flag = False
                break
            else:
                cnt += dict[i]

        if flag:
            answer.append(cnt)
        else:
            answer.append(-1)
    return answer