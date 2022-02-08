def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        # array 에서 범위는 i, j
        n = array[i - 1:j]
        a = list(sorted(n))
        # subarray = sorted(array[i - 1:j]

        answer.append(a[k - 1])

    return answer

# 좋아요 순
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1: x[1]])[x[2] - 1], commands))



