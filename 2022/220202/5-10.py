# # 음료수 얼려 먹기
# n, m = map(int, input().split())
# ice = []
# icecream = 0
#
# # 얼음틀 정보 입력 받기
# for i in range(n):
#     ice.append(list(map(int, input().split())))
#
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if ice[x][y] == 0:
#         ice[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             icecream += 1
#
# print(icecream)
#
#
# n, m = map(int, input().split())
# ice = []
#
# for i in range(n):
#     ice.append(list(map(int, input())))
#
# def dfs(x, y):
#     if x <= -1 or y <= -1 or x >= n or y >= m:
#         return False
#     if ice[x][y] == 0:
#         ice[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)

'''
4 5
00110
00011
11111
00000
'''

n, m = map(int, input().split())
ice = []

for i in range(n):
    ice.append(list(map(int, input())))

def find_ice(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        find_ice(x - 1, y)
        find_ice(x + 1, y)
        find_ice(x, y - 1)
        find_ice(x, y + 1)
        return True
    return False

icecream = 0
for i in range(n):
    for j in range(m):
        if find_ice(i, j) == True:
            icecream += 1

print(icecream)




















