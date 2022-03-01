# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    p_lst = []
    cnt = 0

    for progress, speed in zip(progresses, speeds):
        p_lst.append([progress, speed])

    for p, s in p_lst:
        while p < 100:
            p += s
            if p >= 100: