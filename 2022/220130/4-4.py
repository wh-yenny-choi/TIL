# 게임 개발
'''
현재 위치 기준점 잡고 왼쪽 방향
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
answer = 0

# 방문 위치 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 전체 맵 정보 입력받기
for i in range(n):
    array_list = list(map(int, input().split()))
    array.append(array_list)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 있다면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][dy] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답만 출력
print(count)