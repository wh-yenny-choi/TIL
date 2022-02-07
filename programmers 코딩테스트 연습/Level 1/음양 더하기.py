# def solution(absolutes, signs):
#     answer = 0
#
#     for i in range(len(absolutes)):
#         if signs[i]:
#             answer += absolutes[i]
#         else:
#             answer -= absolutes[i]
#
#     return answer
#
#
# # zip() 함수 : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수. 여러 그룹의 데이터를 동시에 반복문으로 처리할 수 있다. 가장 짧은 데이터 길이만큼 반복된다.
# def solution(absolutes, signs):
#     answer = 0
#
#     for abs, sign in zip(absolutes, signs):
#         if sign:
#             answer += abs
#         else:
#             answer -= abs
#
#     return answer

a = ['a1', 'b1', 'c3']

# 1)
for i in enumerate(a):
    print(i)
