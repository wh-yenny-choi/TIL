def solution(num):
    if num % 2 == 0:  #짝수
        return 'Even'
    else:
        return 'Odd'

# 좋아요 순
def evenOrOdd(num):
    if (num%2):
        return "Odd"  # 홀수일 때 출력값
    else:
        return "Even"
'''
num % 2가 거짓(0)이라면 num % 2 ==0 (거짓) and Odd 가 되므로, 둘 다 참이어야하는 조건에 맞지 않기 때문에 
or Even으로 해서 둘 중에 하나라도 참일 때 가능한 Even이 출력되며 , num%2가 1(참)이면 and 조건이 성립되어 Odd가 출력됩니다


and연산자는 결과값이 둘다 참이여야지 True를 출력하고요 or은 둘중하나만 참이여도 True를 출력합니다 
파이썬은 예외적으로 소괄호를 써서 우선순위를 뒤로 미루는 경우를 제외하고는 먼저써진순서대로 우선처리순위를 잡기때문에 저런 공식이 성립할수 있습니다
'''

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]

'''
& 연산자로 비트 연산한 후 그 수가 ["Even", "Odd"] 배열의 인덱스가 된거군요. 잘 배우고 갑니다:)
2진 비트가 1번째 비트자리에 의해 홀짝이 결정되니 & 연산자로 0 과 1을 구해 리스트 인덱스로 된건가요. 한자리 수는 한자리 비트만 연산되는걸 배우네요 ㅎ
'''