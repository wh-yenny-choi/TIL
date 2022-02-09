# 런타임 에러
def solution(n):
    answer = 0
    for n in range(2, n+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            answer += 1
    return answer

# 효율성 테스트 통과 코드
'''
에라토스테네스의 체
n까지의 모든 소수를 구한다고 하면, 
2를 제외한 2의 배수를 num에서 제거
3를 제외한 3의 배수를 num에서 제거
5를 제외한 5의 배수를 num에서 제거
이렇게 반복해서 num에 남아있는 수들이 소수이다. 
대량의 소수를 한꺼번에 판별하고자 할 때 사용
'''
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)