def solution(n):
    answer = ''

    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)

        return int(answer, 3)