# 오답
def solution(participant, completion):
    answer = 0

    for i in participant:
        if i not in completion:
            answer = i
            break

        if answer == 0:  # 동명이인 경우
            for j in participant:
                if i == j:
                    answer = i

            print(answer)

    return answer


def solution(participant, completion):
    answer = 0

    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion):
        if i != j:
            return i

    return participant.pop()


# collections 활용

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]