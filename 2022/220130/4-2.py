# 시각
h = int(input())
answer = 0

for i in range(h + 1):  # 시는 24
    for j in range(60):  # 분 60
        for k in range(60):  #초 60
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)


hour = int(input())
answer = 0

for i in range(hour + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)

























