def solution(a, b):
    answer = 0

    if a <= b:
        for i in range(a, b + 1):
            answer += i
    else:
        for i in range(a, b - 1, -1):
            answer += i

    return answer

# 좋아요 순
def adder(a, b):
    # 함수를 완성하세요
    if a > b:
        a, b = b, a

    return sum(range(a,b+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(adder(3, 5))

'''
수열 공식 n(n+1)/2 를 이용
'''
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

print( adder(3, 5))