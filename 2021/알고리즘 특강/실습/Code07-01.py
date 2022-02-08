# 큐의 초기화
# 크기가 5칸인 큐의 생성과 데이터 3개 입력

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# 삽입
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print(queue)

# 큐에서 데이터 추출
front += 1
data = queue[front]
queue[front] = None
print('추출 -->', data)

front += 1
data = queue[front]
queue[front] = None
print('추출 -->', data)

front += 1
data = queue[front]
queue[front] = None
print('추출 -->', data)

print(queue)
