def solution(n):
    answer = 0
    n_bin = bin(n)[2:]
    count_n_bin = n_bin.count('1')

    while True:
        n += 1
        count = bin(n)[2:].count('1')
        if count_n_bin == count:
            answer = n
            break

    return answer

# 좋아요 순
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n