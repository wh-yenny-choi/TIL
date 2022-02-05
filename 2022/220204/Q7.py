n = input()
length = len(n)
summary = 0

# 왼쪽 오른쪽 자리수가 같은 위치가 중간값
for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('luck')
else:
    print('ready')




n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])


























