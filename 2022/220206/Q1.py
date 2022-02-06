# 모험가 길드
'''
모험가 n명 공포도 X인 모험가는 반드시 X명이상으로 구성함 모험가 그룹 참여. 최대 그룹 수?
n, x, result, count
if n == x: result += 1
5
2 3 1 2 2
'''
n = int(input())
x = list(map(int, input().split()))
count = 0
result = 0
x.sort(reverse=True)

for i in x:
    count += 1
    if count == x[i]:
        result += 1
        count = 0

print(result)


n = int(input())
x = list(map(int, input().split()))
count = 0
result = 0
x.sort()

for i in x:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)