def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:  # skill_tree 하나씩 확인
            if s in skill:  # 문자 원소 하나씩 확인
                if s != skill_list.pop(0):  # CBD하나씩 꺼내면서 비교, 만약 CBD순서가 맞지 않다면 종료
                    break
        else:
            answer += 1
    return answer