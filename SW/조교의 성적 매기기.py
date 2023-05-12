T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = []

    for mid, last, home in arr:
        sum = mid * 0.35 + last * 0.45 + home * 0.2
        score.append(sum)

    # 내가 찾으려는 타겟의 성적 값 추출
    target = score[K-1]

    # 내림차순 정렬
    score.sort(reverse=True)

    # 총 성적 리스트 중 타겟의 위치를 뽑은 후, N명씩 성적을 끊는 거니 무슨 rank인지 찾을 수 있음
    rank = score.index(target) // (N//10)

    tg = grades[rank]

    print('#{} {}'.format(t, tg))