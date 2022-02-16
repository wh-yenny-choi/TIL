# 오답
'''
방문처리 방법에서 오답
'''
def solution(dirs):
    answer = 0
    count = 0
    first = []

    x, y = 0, 0
    move_type = ['L', 'R', 'U', 'D']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for dir in dirs:
        for i in range(len(move_type)):
            if dir == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                count += 1
                answer = count

                first.append((nx, ny))
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            count -= 1
            continue
            answer -= count
        x, y = nx, ny

    # 처음걸어본 길

    # print(test)
    return answer

# 처음 걸어본 길 구글링 도움
def solution(dirs):
    answer = 0
    x, y = 0, 0
    move_type = ['L', 'R', 'U', 'D']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = set()

    for dir in dirs:
        for i in range(len(move_type)):
            if dir == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 범위 벗어난 경우 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        # 처음 걸어본 길
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))  # set() 중복값 제거하면서 추가
            visited.add((nx, ny, x, y))  # 길은 '양방향' 임을 빼먹으면 안됨!
            answer += 1
        # 이동
        x, y = nx, ny

    return answer


# 좋아요 순
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2