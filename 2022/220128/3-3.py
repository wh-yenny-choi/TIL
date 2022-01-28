'''
3 3
3 1 2
4 1 4
2 2 2
'''
# n, m = map(int, input().split())
# card = []
#
# for i in range(n):
#     card.append(list(map(int, input().split())))
#
# # 리스트 각 열마다 가장 작은 숫자 확인
# # 각 열의 가장 작은 숫자 중 가장 큰 숫자 찾기
# for i in card[0]:
#

# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)


n, m = map(int, input().split())
result = 0

for i in range(n):
    cards = list(map(int, input().split()))
    # 각 줄에서 최솟값 찾기
    min_value = min(cards)
    # 최솟값 중 가장 큰 값 찾기
    result = max(result, min_value)

print(result)





















