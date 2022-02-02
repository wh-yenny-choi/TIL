# 미로 탈출
'''
5 6
101010
111111
000001
111111
111111

3 3
110
010
011
'''
# n, m = map(int, input().split())
# x, y = 1, 1
# maze = []
#
# for i in range(n):
#     maze.append(list(map(int, input())))
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# answer = 1
# while maze[x][y] > 0:
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if maze[nx][ny] == 1:  # 괴물이 없다면 x, y 이동 후 기록
#             maze[nx][ny] = 0
#             x = nx
#             y = ny
#             answer += 1
#         if maze[nx][ny] == 0:  # 괴물이 있는 경우 무시
#             continue
#         if nx < 0 or ny < 0 or nx >= n or nx >= m:
#             continue
#
# print(answer)
#
# from collections import deque
#
# n, m = map(int, input().split())
# maze = []
#
# for i in range(n):
#     maze.append(list(map(int, input())))
#
# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if maze[nx][ny] == 0:  # 괴물 존재한다면 무시
#                 continue
#             if maze[nx][ny] == 1:  # 괴물 존재하지 않는다면 기록
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 변환
#     return maze[n - 1][m - 1]
#
# print(bfs(0, 0))
#

from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
            
            
    return maze[n - 1][m - 1]

print(bfs(0, 0))
