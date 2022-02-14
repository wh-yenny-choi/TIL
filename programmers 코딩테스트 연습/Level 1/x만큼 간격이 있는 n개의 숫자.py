def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)

    return answer

# 좋아요 순
def number_generator(x, n):
    return [i * x + x for i in range(n)]

def number_generator(x, n):
    return [i for i in range(x, x*n+1, x)]
