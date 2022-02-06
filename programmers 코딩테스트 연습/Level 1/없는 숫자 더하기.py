def solution(numbers):
    answer = 0  # 없는 숫자

    for i in range(10):
        if i not in numbers:
            answer += i

    return answer