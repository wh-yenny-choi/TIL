def solution(num):
    answer = 0

    while num > 1:
        if num % 2 == 0:
            num //= 2
            answer += 1
            continue
        if num % 2 != 0:
            num = (num * 3) + 1
            answer += 1
            continue
        if num == 1:
            break
    if answer >= 500:
        answer = -1
    return answer

# 좋아요 순
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1