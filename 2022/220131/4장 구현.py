# # 상하좌우
# n = int(input())
# plans = input().split()
# x, y = 1, 1
#
# move_type = ['L', 'R', 'U', 'D']
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# for plan in plans:
#     for i in range(len(move_type)):
#         if plan == move_type[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > x or ny > y:
#         continue
#     x, y = nx, ny
#
# print(x, y)
#
# 시각
# hour = int(input())
# answer = 0
#
# for i in range(hour + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 answer += 1
#
# print(answer)
#
# 왕실의 나이트
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]
#
# answer = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         answer += 1
#
# print(answer)
#
# 게임개발
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
n, m = map(int, input().split())
a, b, direction = list(map(int, input().split()))
map_info = []

for i in range(n):
    map_info.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 북동남서
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

d = [[0] * m for _ in range(n)]

d[a][b] = 1  # 현재위치 방문 처리

# 맵 안에서 이동
answer = 1  # 캐릭터가 방문한 칸의 개수
turn_count = 0  # 회전한 횟수
while True:
    turn_left()
    na = a + da[direction]
    nb = b + db[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[na][nb] == 0 or map_info[na][nb] == 0:
        d[na][nb] = 1
        a, b = na, nb
        answer += 1  # 회전 1회 후 직진 => 방문한 칸의 개수는 증가
        turn_count = 0  # 회전 횟수는 그대로 0
        continue

    # 왼쪽 방향에 가보지 않은 칸이 없는 경우, 왼쪽 방향으로 회전만 수행
    else:
        turn_count += 1

    # 네방향 모두 가본칸인 경우에는 바라보는 방향 유지한 채 한 칸 뒤로 가고 1단계로 돌아감
    if turn_count == 4:
        na = a - da[direction]
        nb = b - db[direction]
        # 뒤쪽 방향이 바다인 경우에는 움직임을 멈추고, 육지면 뒤로 이동
        if map_info[na][nb] == 0:
            a, b = na, nb
        else:
            break
        turn_count = 0

print(answer)

