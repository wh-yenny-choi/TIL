# https://programmers.co.kr/learn/courses/30/lessons/42586
# def solution(progresses, speeds):
#     answer = []
#     p_lst = []
#     cnt = 0
#
#     for progress, speed in zip(progresses, speeds):
#         p_lst.append([progress, speed])
#
#     for p, s in p_lst:
#         while p < 100:
#             p += s
#             if p >= 100:

def solution(progresses, speeds):
    answer = []
    cnt = 0

    while progresses:
        # 100 이상인 경우를 꺼내고, 배포카운트 1 증가
        if progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            cnt += 1
        else:  # 100 미만일 때
            # 배포 카운트가 0이상인 경우, 그 동안 증가된 배포 카운트를 정답에 저장
            if cnt > 0:
                answer.append(cnt)
            cnt = 0  # 배포카운트 초기화
            # 전체 배열을 순회하며 속도만큼 값을 누적
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
    # 마지막으로 남은 배포카운트가 있다면 정답에 저장
    if cnt > 0:
        answer.append(cnt)

    return answer