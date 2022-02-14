# 오답
def solution(s):
    answer = []
    n = s.split(' ')

    for i in n:
        for j in range(len(i)):
            if j == 0:
                n = i[j].upper()
            if j % 2 == 0:  # 짝수번쨰는 대문자
                n = i[j].upper()
            if j % 2 != 0:  # 홀수번째는 소문자
                n = i[j].lower()
            answer.append(n)
    answer = ''.join(answer)

    return answer
'''
실행한 결괏값 "TrYHeLlOWoRlD"이(가) 기댓값 "TrY HeLlO WoRlD"와(과) 다릅니다.
띄어쓰기는...?
'''

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