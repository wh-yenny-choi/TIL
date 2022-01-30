'''
5
R R R U D D
'''

# n = int(input())
# char = input()
# answer = 0  # 최종 도착 지점 좌표
#
# # LRUD 좌표 설정
# # 예외처리 -> 좌표 밖으로 벗어난 경우
# dx = [0 , 1, 0, -1]
# dy = [-1, 0 , 1, 0]
#
# # n번 동안
# for i in range(n):
#     if i == 'R':
#         nx = dx + dx[i]
#         ny = dy + dy[i]
#     while dx >= 0 and dy >= 0:

# n = int(input())
# x, y = 1, 1  # 최종 도착 지점 좌표
# char = input().split()
#
# # LRUD 좌표 설정
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# # 이동 계획을 하나씩 확인
# for plan in char:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
#
# print(x, y)


#################################
# n = int(input())  # 공간 크기 n 입력 받기
# x, y = 1, 1  # 시작 좌표는 항상 1, 1
# plans = input().split()  # 문자 입력 받기
#
# # L, R, U, D 입력받기
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# char = ['L', 'R', 'U', 'D']
#
# # 입력 받은 문자를 확인하면서
# for plan in plans:
#     # 이동하기
#     for i in range(len(char)):
#         if plan == char[i]:  # 입력받은 문자와 같다면
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간 크기 범위를 벗어나는 경우 예외처리
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x, y)
#####################################################
# n = int(input())
# plans = input().split()
# x, y = 1, 1
#
# # 상하좌우 설정
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# move_type = ['L', 'R', 'U', 'D']
#
# # 최종 좌표 찾기
# # 입력 받은 문자에 따라서 이동
# for plan in plans:
#     # 입력받은 문자와 move_type이 같다면 상하좌우 이동
#     if plan == 'L':
#         nx = x + dx[0]
#         ny = y + dy[0]
#     if plan == 'R':
#         nx = x + dx[1]
#         ny = y + dy[1]
#     if plan == 'U':
#         nx = x + dx[2]
#         ny = y + dy[2]
#     if plan == 'D':
#         nx = x + dx[3]
#         ny = y + dy[3]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
# print(x, y)
###################################################
n = int(input())
plans = input().split()
x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)