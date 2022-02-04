from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 벗어나면 무시
                continue
            if maze[nx][ny] == 0:  # 괴물 존재시
                continue  # 무시
            if maze[nx][ny] == 1:  # 괴물 존재하지 않으면
                maze[nx][ny] = maze[x][y] + 1
                queue.append((x, y))
    return maze[n - 1][m - 1]  # 가장 오른쪽 아래까지

print(bfs(0, 0))