## 재귀 호출 함수 기본(반환 조건 추가)

# 함수 선언
def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('### 반지 넣기 ###')
        return
    openBox()
    print('상자 닫기')


# 전역 변수
count = 10

# 메인 코드
openBox()

'''
## 실습 ##
# 함수 선언
def openBox():
    global count
    print('박스 열기')
    count -= 1
    if(count == 0):
        print('*** 반지 넣기 ***')
        return
    openBox()
    print('박스 닫기')

count = 10
openBox()
'''














