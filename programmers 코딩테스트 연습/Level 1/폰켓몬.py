def solution(nums):
    answer = 0
    choice = len(nums) // 2
    ponketmon = list(set(nums))

    if len(ponketmon) > choice:
        answer = choice
    else:
        answer = len(ponketmon)

    return answer


# 조합 사용 -> 런타임 에러
from itertools import combinations
def solution(nums):
    answer = 0
    choice = len(nums) // 2

    for i in combinations(nums, choice):
        # 가장 많은 종류의 폰켓몬을 선택하는 방법
        if answer < len(set(i)):
            answer = len(set(i))
    return answer