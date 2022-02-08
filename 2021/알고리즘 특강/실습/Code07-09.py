## 큐가 꽉 찼는지 확인하는 함수 개선 버전

# 함수 선언부
# 큐가 꽉찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE - 1) and (front == -1):
        return True
    else:
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 큐가 비었는지 체크하는 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

# 큐에 데이터를 삽입하는함수
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉참')
        return
    rear += 1
    queue[rear] = data

# 큐에서 데이터를 추출하는 함수
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 비었음')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 전역 변수 부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# # 메인 코드 부
# queue = ['화사', '솔라', '문별', '휘인', '선미']
# front = -1
# rear = 4
# print('큐 꽉참?', isQueueFull())
# print('큐 비었음?', isQueueEmpty())

print(queue)
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
enQueue('재남')
print(queue)
retData = deQueue()
print(retData)
retData = deQueue()
print(retData)
print(queue)
enQueue('원희')
print(queue)

