n, m = map(int, input().split())
x, y, direction = map(int, input().split())
data = []  # 맵 정보

for i in range(n):  # 맵 정보 입력받기
    data.append(list(map(int, input().split())))

# n x m 맵 정보 초기화 (0 = 방문하지 않음, 1 = 방문 처리 완료)
d = [[0] * m for _ in range(n)]
# 북, 동, 남, 서 좌표 입력
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d[x][y] = 1  # 처음 1, 1은 방문처리

# 왼쪽 방향 설정
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1  # 캐릭터가 방문한 칸의 수
turn_count = 0  # 방향 회전 수
while True:
    # 1. 현재 위치에서 왼쪽 방향 부터 갈 곳을 정한다
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 2. 왼쪽에 가보지 않은 칸이 있다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진한다.
    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    # 2. 왼쪽 방향으로 모든 칸을 방문했다면, 회전만 수행하고 1번으로 돌아간다.
    else:
        turn_count += 1
    # 3. 네 칸 모두 가본 칸이거나 바다로 되어 있다면, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1번으로 돌아간다.
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        turn_count = 0
        if data[nx][ny] == 0:  # 뒤로 갈 수 있다면 (0 = 육지) 이동하기
            x = nx
            y = ny
    # 3. 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
        else:
            break

print(count)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''