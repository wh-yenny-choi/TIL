def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)  # B.reverse()

    for i, j in zip(A, B):
        answer += i * j

    return answer

# 좋아요 순
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))