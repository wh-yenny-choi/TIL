def solution(s):
    answer = []
    split_s = s.split(' ')

    for i in split_s:
        result = ''
        for j in range(len(i)):
            result += i[j].lower()
            if j == 0:
                result = i[j].upper()
        answer.append(result)

    return ' '.join(answer)

# 좋아요 순
def Jaden_Case(s):
    return s.title()
#  s.title()이 아니라 s.lower().title()

def Jaden_Case(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

def Jaden_Case(s):
    list1 = s.split()
    for x, y in enumerate(list1):
        list1[x] = y.capitalize()
    return ' '.join(list1)

def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize()
        else:
            answer += ' '+i.capitalize()
    return answer

# level1. 이상한 문자 만들기
def solution(s):
    answer = []
    n = s.split(' ')

    for i in n:
        new = ''  # 새로운 문자열 생성
        for j in range(len(i)):
            if j % 2 == 0:  # 짝수번쨰는 대문자
                new += i[j].upper()  # 결과값을 새로운 문자열에 붙이기
            if j % 2 != 0:  # 홀수번째는 소문자
                new += i[j].lower()
        answer.append(new)
    answer = ' '.join(answer)  #띄어쓰기를 기준으로 다시 문자를 붙여준다
    return answer

# 좋아요 순
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])