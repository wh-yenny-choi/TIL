def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return (f"{answer / len(arr)}")

# 좋아요 순
def average(list):
    return (sum(list) / len(list))

# 람다 이용
from functools import reduce
def average(list):
    return reduce(lambda x, y : x + y, list) / len(list)

# statistics
import statistics
def average(list):
    return statistics.mean(list)