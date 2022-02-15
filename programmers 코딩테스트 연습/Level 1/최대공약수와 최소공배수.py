# def solution(n, m):
#     answer = []
#     # m이 n으로 나누어 진다면 나누어진 몫이랑 n을 곱해서 리턴
#     if m % n == 0:
#         while m % n == 0:
#             max = m // n
#             answer.append(n)
#             answer.append(max * n)
#             break
#         return answer
#     # 아니면 그냥 n*m
#     if m % n != 0:  # 나누어 떨어지지 않는다면
#         answer.append(1)
#         answer.append(n*m)
#         return answer
def lcm(n, m):
    return n*m / math.gcd(n, m)

import math
def solution(n, m):
    max = math.gcd(n, m)
    min = lcm(n, m)
    return (max, min)

# 좋아요 순
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
