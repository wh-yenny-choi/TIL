# 첫번째 - 오답
def solution(answers):
    result = []  # 제일 많이 맞춘 사람

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_cnt = 0
    second_cnt = 0
    third_cnt = 0

    for answer, f, s, t in zip(answers, first, second, third):
        if answer == f:
            first_cnt += 1
        if answer == s:
            second_cnt += 1
        if answer == t:
            third_cnt += 1

    num = max(first_cnt, second_cnt, third_cnt)
    if num == first_cnt:
        result.append(1)
    if num == second_cnt:
        result.append(2)
    if num == third_cnt:
        result.append(3)

    return result


# 구글링 도움 1 - for문 수정
def solution(answers):
    result = []  # 제일 많이 맞춘 사람

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_cnt = 0
    second_cnt = 0
    third_cnt = 0

    for i in range(len(answers)):
        if answers[i] == first[(i % 5)]:
            first_cnt += 1
        if answers[i] == second[(i % 8)]:
            second_cnt += 1
        if answers[i] == third[(i % 10)]:
            third_cnt += 1

    num = max(first_cnt, second_cnt, third_cnt)
    if num == first_cnt:
        result.append(1)
    if num == second_cnt:
        result.append(2)
    if num == third_cnt:
        result.append(3)

    return result

# 구글링 전문
def solution(answers):
    answer = []
    counts = [0, 0, 0]

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first[(i % 5)]:
            counts[0] += 1
        if answers[i] == second[(i % 8)]:
            counts[1] += 1
        if answers[i] == third[(i % 10)]:
            counts[2] += 1

    for i in range(3):
        if counts[i] == max(counts):
            answer.append(i + 1)

    return answer