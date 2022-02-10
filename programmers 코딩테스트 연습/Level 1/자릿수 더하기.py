'''
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
'''
def solution(n):
    answer = 0
    array = []

    for i in range(len(str(n))):
        array.append((str(n)[i]))

    for j in array:
        answer += int(j)

    return answer
'''
자연수의 길이를 확인 => 숫자를 str 함수를 통해 문자열로 바꾸고, 여기에 len 내장함수를 통해 그 길이를 반환하면 이 기능을 완벽하게 구현할 수 있다. 
                     ex) len(str(n))

자연수의 인덱스를 확인 => 숫자를 str함수를 통해 문자열로 바꾸고, 인덱스 반환
                      ex) str(n)[0]  ( 내가 실수한 점: str(n[0]) )
'''

# 좋아요 순
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)   # 재귀함수 이용

def sum_digit(number):
    return sum([int(i) for i in str(number)])

def sum_digit(number):
    return sum(map(int, str(number)))