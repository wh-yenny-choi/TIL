# 동전 0
'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력 예시
-------------
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
-------------
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
-------------
'''
n, k = map(int, input().split())
coin_list = []
count = 0
coin_count = 0

for i in range(n):
    coin_list.append(input())

for coin in coin_list[::-1]:
    if int(coin) > k:
        continue
    else:
        count = k // int(coin)
        coin_count += count
        k %= int(coin)
print(coin_count)