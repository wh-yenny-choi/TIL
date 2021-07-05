## 스택에 데이터를 삽입하는 함수

# 함수 선언 부분
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('스택 꽉참')
        return
    top += 1
    stack[top] = data

# 전역 변수
SIZE = 5
#stack = [None for _ in range(SIZE)]
stack = ['커피', '녹차', '꿀물', '콜라', None]
#top = -1
top = 3

print(stack)
push('환타')
print(stack)
push('사이다')
print(stack)