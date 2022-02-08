## 숫자 합계 내기 (1부터 10까지 합계 구하기)

# 반복문을 이용한 구현
sumValue = 0
for n in range(10, 0, -1):
    sumValue += n
print('합은', sumValue)

# 재귀 호출로 구현
def addNumber(num):
    if num < -1:
        return 1
    return num + addNumber(num - 1)
print(addNumber(10))


## 팩토리얼 구하기(10부터 1까지 곱하기)
# 반복문 이용한 구현
factValue = 1  # 곱셈이므로 초깃값을 1로 설정
for n in range(10, 0, -1):
    factValue *= n
print("\n곱은", factValue)

# 재귀 호출 과정을 재귀 함수로 작성
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
print('10!=',factorial(10))


## 카운트다운을 재귀 호출로 구현
print()
def countDown(count):
    if count == 0:
        print('발사')
    else:
        print(count)
        countDown(count - 1)

count = 5
countDown(count)


## 별 모양 출력대로 재귀 호출 구현
print()
def printStar(n):
    if n > 0:
        printStar(n - 1)
        print('★' * n)

printStar(5)


## 구구단 출력을 재귀 호출로 구현
print()
def gugu(dan, num):
    print('{} * {} = {}' .format(dan, num, dan*num))
    if num < 9:
        gugu(dan, num + 1)

for dan in range(2, 10):
    print(f' ೄ✲ﾟ*｡✧{dan}단ೄ✲ﾟ*｡✧')
    gugu(dan, 1)


## N제곱 계산을 재귀 호출로 구현
print()
tab = ''
def pow(x, n):
    global tab
    tab += ' '
    if n == 0:
        return 1
    print(tab + '%d * %d ^(%d - %d)' %(x, x, n, 1))
    return x * pow(x, n - 1)

print('2 ^ 4')
print('답 :', pow(2, 4))


## 배열의 합계를 재귀 호출로 구현 (실행 결과는 실행할 때마다 다름)
print()
import random

def arySum(arr, n):
    if n <= 0:
        return arr[0]
    return arySum(arr, n - 1) + arr[n]

ary = [random.randint(0, 255) for _ in range (random.randint(10, 20))]
print(ary)
print('배열 합계 :', arySum(ary, len(ary) - 1))
