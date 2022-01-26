# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)  # 큰 수 나열
# result = 0
#
# # 제일 큰수를 k번 동안 -> k 번 이후에는 그다음 큰수 후 초기화 -> K다시 반복
# while True:
#     for i in range(k):  # 총 더해지는 k번
#         if m == 0:  # 연속되는 수가 0이면 초기화
#             break
#         result += data[0]
#         m -= 1
#     if m == 0:
#         break
#     result += data[1]
#     m -= 1
#
# print(result)
#
# # n = 배열의 크기, m = 숫자가 더해지는 횟수, k = 연속해서 더해지는 횟수
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
#
# result = 0
#
# # m이 0이 될까지 k개 안에서 더하기
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += data[0]  # 결과값에 가장 큰 수 k번 동안 더하기
#         m -= 1  # 더할때마다 총 기회 횟수 -1씩
#     if m == 0:
#         break
#     # k개 다 쓰면 두번째 큰 수를 결과값에 더하기
#     result += data[1]
#     m -= 1
#
# print(result)
#
#
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
#
# result = 0  # 가장 큰 수 결과
#
# # k번 더하고, 다 더하면 그 다음 큰수로 더하기 (m이 0이 되기전까지)
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += data[0]  # k반복문 안에서 가장 큰 수 더하기
#         m -= 1  # 최종 더할 수 있는 횟수 -1
#     if m == 0:
#         break
#     result += data[1]
#     m -= 1
#
# print(result)


'''
시간 복잡도 개선
----------------------------------------------------------------------------
'''
n, m, k = map(int, input().split())  # 5 8 3
data = list(map(int, input().split()))

data.sort(reverse=True)

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k  # 반복되는 수열의 길이 = m / (k + 1)로 나눈 몫이 수열이 반복되는 횟수, 가장 큰 수가 등장하는 횟수 = m / (k + 1) * k
count += m % (k + 1)  # m이 (k + 1)로 나누어 떨어지지 않는 경우 고려 -> m / (k + 1) 로 나눈 나머지만큼 가장 큰 수가 추가로 더해짐

result = 0
result += (count) * data[0]  # 가장 큰 수 더하기
result += (m - count) * data[1]  # 두 번째로 큰 수 더하기

print(result)