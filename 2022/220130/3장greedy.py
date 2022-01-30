# 3-1 거스름돈
n = 1260
coins = [500, 100, 50, 10]
answer = 0  # 거슬러 줘야 할 동전의 최소 개수

for coin in coins:
    answer += n//coin
    n %= coin

print(answer)

# 3-2 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

data.sort(reverse=True)

while m > 0:
    for i in range(k):
        answer += data[0]
        m -= 1
    answer += data[1]
    m -= 1

print(answer)

# 3-3 숫자 카드 게임
n, m = map(int, input().split())
answer = 0

for i in range(n):
    cards = list(map(int, input().split()))
    min_value = min(cards)
    max_value = max(answer, min_value)

print(max_value)

# 1이 될 때까지
n, k = map(int, input().split())
answer = 0

while n > 1:
    if n % k == 0:  # 나머지가 0 ==> 나누어 떨어진다
        n //= k
        answer += 1
    else:
        n -= 1
        answer += 1

print(answer)
