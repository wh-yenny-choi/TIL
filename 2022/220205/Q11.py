n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
data = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

L = int(input())  # 변환 횟수
L_info = []
for i in range(L):
    x, c = map(int, input().split())
    L_info.append((int(x), c))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2  # 뱀 존재 위치는 2로 표시
    direction = 0  # 처음에는 동쪽 보고 있음
    time = 0
    index = 0
    q = [(x, y)]
