# 오답
'''
s가 1의 자리수면 작동
'''
def solution(s):
    answer = []

    for i in range(len(s)):
        max = s[:1]
        min = s[-1:]
        if s[0] == '-':
            max = s[-2:]
            min = s[:2]
    answer.append(max)
    answer.append(min)
    answer = ' '.join(answer)

    return answer


def solution(s):
    answer = []
    max = 0
    min = 0
    # str을 공백 기준으로 나누기
    split_s = s.split(' ')

    max = str(split_s[:1])
    min = str(split_s[-1:])

    if split_s[0] == '-':
        min = str(split_s[:1])
        max = str(split_s[-1:])

    answer.append((max, min))
    answer = ''.join(answer)

    # for i in split_s:
    # max = split_s[:1]
    # min = split_s[-1:]
    # if i[0] == '-':
    #     min = split_s[:1]
    #     max = split_s[-1:]
    # answer.append((max, min))
    # print(type(str(max)))
    # print(min)
    # answer.append(str(max))
    # answer.append(str(min))
    # answer = ''.join(answer)

    # for i in range(len(s)):
    #     max = s[:1]
    #     min = s[-1:]
    #     print(type(min))
    #     if s[0] == '-':
    #         max = s[-2:]
    #         min = s[:2]
    # print(type(min))
    # answer.append(max)
    # answer.append(min)
    # answer = ' '.join(answer)

    return answer


def solution(s):
    answer = ''
    split_s = s.split(' ')

    new_s = list(map(int, split_s))
    max_s = max(new_s)
    min_s = min(new_s)

    answer = str(min_s) + ' ' + str(max_s)
    return answer