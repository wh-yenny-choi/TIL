def solution(n):
    answer = []

    for x in range(2, 1000000):
        if n % x == 1:
            answer.append(x)

    return answer[0]

'''
for x in range(3, 1000000)일때 오류 해결
n의경우 3부터 시작하므로 n-1의 경우는 2부터 시작해서 
저도 n-1을 3부터 시작했더니 3,4번 문제가 오류나서 수정하니 풀렸네요
'''

# 간단한 풀이
def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer