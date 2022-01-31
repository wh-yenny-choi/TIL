# 팩토리얼
def fac(n):
    result = 1
    for i in range(1, n + 1, 1):
        result *= i
    return result

print(fac(5))

# 팩토리얼
def fact(n):
    if n <= 1:
        return 1
    count = n * fact(n - 1)
    return count

print(fact(5))