n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = 0  # 최댓값

# 가장 큰 수 k번 더하고 k가 0이 되면 그 다음 큰 수 k번 더하기
while True:
    for i in range(k):
        if m == 0:
            break
        result += data[0]
        m -= 1
    if m == 0:
        break
    result += data[1]
    m -= 1

print(result)