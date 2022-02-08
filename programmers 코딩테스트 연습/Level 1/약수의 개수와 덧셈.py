def divisor(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if len(divisor(i)) % 2 == 0:  # 짝수
            answer += i
        else:
            answer -= i

    return answer


# 약수가 홀수개인 모든 수는 제곱수
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

# math
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer