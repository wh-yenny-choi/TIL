# 오답
def solution(d, budget):
    answer = 0  # 최대 물품 개수
    count = 0

    # d각 원소의 합이 budget 내에 있을 때 최대 개수
    for i in range(len(d)):
        count += d[i]
        if count > budget:
            break
        else:
            answer += 1

    return answer

# 해결 -> d.sort()
def solution(d, budget):
    answer = 0  # 최대 물품 개수
    count = 0  # 리스트d의 각 원소의 합

    d.sort()
    # d각 원소의 합이 budget 내에 있을 때 최대 개수
    for i in range(len(d)):
        count += d[i]
        if count > budget:
            break
        else:
            answer += 1

    return answer


# 좋아요 순
def solution(d, budget):
    d.sort()
    while budget < sum(d):  # 예산내로 들어올때까지
        d.pop()  # 예산 넘는 합은 계속해서 제거
    return len(d)  # 남는 d는 예산 내에서의 최대 합