# 오답
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer
'''
i = 0일때의 값이 생략되는 문제 발생 => 첫번째 원소 리스트에 추가
'''

# 해결
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer