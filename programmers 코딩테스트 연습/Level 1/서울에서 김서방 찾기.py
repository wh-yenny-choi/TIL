# index() 사용
def solution(seoul):
    answer = seoul.index('Kim')
    return "김서방은 {}에 있다".format(answer)

# enumerate() 사용
def solution(seoul):
    for index, name in enumerate(seoul):
        if name == 'Kim':
            answer = '김서방은 '+str(index)+'에 있다'
    return answer