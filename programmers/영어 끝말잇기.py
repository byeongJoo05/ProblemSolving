"""
결과 : [번호, 차례]
번호 - 사람 번호
차례 - 몇 번째 순회였는지

같은 단어를 말한 사람 or 끝말잇기에 틀린 사람을 골라내서 몇 번째 순회였는지 찾는 문제

1. 틀린 것 골라내기
끝단어 word[-1]을 저장할 변수와 시작단어 word[0] 을 찾아내면 되는거 아닐까?

2. 같은 단어 말한 사람
리스트에 문자 저장해서 있는지 존재 파악하기
"""


def solution(n, words):
    answer = []
    double = [words[0]]
    cnt = 1  # 차례
    person = 2  # 사람
    ch = words[0][-1]

    # 틀렸음을 유도하는 반복문
    for word in words[1:]:

        # 만약 같은 단어를 말했다면?
        if word in double:
            answer.append(person)
            answer.append(cnt)
            print(answer)
            return answer
        else:
            double.append(word)

        if ch != word[0]:
            answer.append(person)
            answer.append(cnt)
            print(answer)
            return answer
        else:
            ch = word[-1]

        # n번째 사람까지 돌았다면 cnt 더해주고
        if person == n:
            cnt += 1
            person = 1
        else:
            person +=1

    return [0, 0]

print (solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print (solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))