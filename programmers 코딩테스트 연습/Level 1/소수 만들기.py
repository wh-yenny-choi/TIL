# 오답
def solution(nums):
    import random
    answer = 0

    while True:
        # nums에 있는 숫자들 중 서로 다른 3개를 골라
        count = random.sample(nums, 3)
        # 더했을 때 소수가 되는 경우의 개수
        for i in range(1, len(nums)):
            if sum(count) % i == 0:
                answer += 1
                continue
            else:
                break

        return answer


def sosu(x):  # 소수 판별 함수
    for i in range(2, (x // 2) + 1):
        if x % i == 0:  # 해당 수로 나누어 떨어진다면
            return False  # 소수가 아님
    return True  # 소수


def solution(nums):
    import itertools
    answer = 0
    # nums에 있는 숫자들 중 서로 다른 3개를 골라
    combi = itertools.combinations(nums, 3)
    # combi = list(combinations(nums, 3))
    print(list(combi))

    # 더했을 때 소수가 되는 경우의 개수
    for i in combi:
        if sosu(sum(i)):
            answer += 1

    return answer


from itertools import combinations  # 중복허용(X), 순서의미(O) 인 조합을 import

"""소수 판별 함수"""


def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num // 2) + 1):  # math를 사용하지 않고 (num//2)+1 까지로 설정
            if num % n == 0:
                return False

        return True


def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))  # nums배열을 3개씩 조합 후 list로 변경
    for arr in cmb:
        if is_prime_number(sum(arr)):  # cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
            answer += 1  # return 값이 True이면 count(=answer) +1

    return answer


from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        s = sum(i)
        result = 0
        for j in range(2, s):
            if s % j == 0:
                result += 1
                break
        if result == 0:
            answer += 1
    return answer


from itertools import combinations


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):  # 서로 다른 3개 골라 더하기
        s = sum(i)
        count = 0
        # 소수가 되는 경우 확인
        for j in range(2, s):  # 1제외한 숫자부터 s-1 까지
            if s % j == 0:  # 소수가 아닌 경우
                count += 1
                break
        if count == 0:  # 소수인 경우
            answer += 1

    return answer