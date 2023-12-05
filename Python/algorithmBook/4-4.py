n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x, y, direction = map(int,input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1 # 반시계방향으로 시선 회전
    if direction == -1: # 북쪽 다음엔 서쪽이므로 direction을 3으로 바꿈
        direction = 3

count = 1 # 첫위치부터 방문칸이므로 1을 추가하고 시작
turn_time = 0 # 캐릭터 회전 수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우에 이동하기
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)