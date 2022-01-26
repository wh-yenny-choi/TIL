n = 1260
count = 0  # 거스름돈

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin  # 카장 큰 화폐 단위부터 거슬러 줄 수있는 거스름돈의 갯수
    n %= coin  # 거슬러 준 이후의 남은 거스름돈

print(count)

n = 1260
count = 0  # 거스름 돈 개수

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)




























