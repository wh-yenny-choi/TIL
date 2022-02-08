# 오답
from itertools import combinations
def solution(numbers):
    answer = []
    array = list(combinations(numbers, 2))
    count = 0

    for i in array:
        count = i[0] + i[1]
        answer.append(count)
        answer.sort()

    result = list(set(answer))

    return result

# 해결
'''
음수가 포함될 때 sort는 양수 -> 음수 순서로 정렬, sorted를 사용하면 음수 -> 양수 순서로 정렬됩니다.
'''
from itertools import combinations
def solution(numbers):
    answer = []
    array = list(combinations(numbers, 2))
    count = 0

    for i in array:
        count = i[0] + i[1]
        answer.append(count)

    return sorted(list(set(answer)))