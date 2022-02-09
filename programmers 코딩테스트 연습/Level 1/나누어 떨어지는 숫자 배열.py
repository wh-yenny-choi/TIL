# 오답
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:  # 나누어 떨어진다면
            answer.append(arr[i])

        if len(answer) == 0:
            answer.append(-1)
        else:
            answer.sort()
    return answer
'''
for문 완료 후에 len의 길이가 0이여야 함
'''

# 정답
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)) :
        if arr[i] % divisor == 0 :
            answer.append(arr[i])
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer