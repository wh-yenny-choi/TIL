def solution(n):  # n = 12345
    answer = list(str(n)[::-1])  # ['5', '4', '3', '2', '1']
    answer = list(map(int, answer))  # [5, 4, 3, 2, 1]
    return answer
'''
리스트의 문자열을 int형태로 변환 => list(map(함수, 리스트))
answer = [int (i) for i in answer]
'''
def solution(n):
    answer = list(str(n)[::-1])
    return [int(i) for i in answer]

# 좋아요 순
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

