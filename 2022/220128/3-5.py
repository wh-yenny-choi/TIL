n, k = map(int, input().split())

count = 0
'''
1. n을 k로 나눈다
2. k로 나누어 지지 않는다면 나누어질때까지 -1 반복
'''
while n >= k:
    if n % k == 0:  # 나머지가 0 => 나누어짐
        n //= k
        count += 1
    else:  # k로 나누어 지지 않는다면
        n -= 1
        count += 1

print(count)

'''답-----------------------------------------------'''
n, k = map(int, input().split())
result = 0

while n >= k:
    # n이 k로 나누어지지 않는 경우
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

    # 마지막 남은 수에 대하여 1씩 빼기
    while n > 1:
        n -= 1
        result += 1

print(result)


'''
시간 복잡도 해결
'''
n, k = map(int, input().split())
result = 0

while True:
    # n == k 로 나누어 떨어질 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)