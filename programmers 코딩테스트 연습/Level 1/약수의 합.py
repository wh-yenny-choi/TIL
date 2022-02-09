def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer


# 좋아요 순
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# lambda이용
def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))