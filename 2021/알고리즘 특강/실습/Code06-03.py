## 스택이 꽉 찼는지 확인하는 함수

# 함수 선언
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False

# 전역 변수
SIZE = 5
#stack = [None for _ in range(SIZE)]
stack = ['커피', '녹차', '꿀물', '콜라', '환타']
#top = -1
top = 4

print('스택 꽉참?', isStackFull())