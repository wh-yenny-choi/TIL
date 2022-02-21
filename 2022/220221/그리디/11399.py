# ATM
'''
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

입력 에시
----------------
5
3 1 4 3 2
----------------
'''
n = int(input())
p = list(map(int, input().split()))
time = 0
answer = 0
result = []

p.sort()
for i in p:
    time += i
    result.append(time)

for j in result:
    answer += j
print(answer)

# 강의 해답 코드
n = int(input())
p = list(map(int, input().split()))
minimum = 0

p.sort()
for index in range(n):
    for index2 in range(index + 1):
        minimum += p[index2]
print(minimum)