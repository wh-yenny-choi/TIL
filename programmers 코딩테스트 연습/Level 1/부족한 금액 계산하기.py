def solution(price, money, count):
    # answer = -1
    total = 0
    result = 0

    for i in range(1, count + 1):
        n_price = price * i
        total += n_price

        if total > money:
            result = total - money
        # else:
            # result = 0

    return result


# 다른 풀이
def solution(price, money, count):
    answer = 0

    for i in range(count):
        temp=price*(i+1)
        answer=answer+temp
    answer=answer-money
    if answer<=0:
        return 0
    return answer

# 좋아요 순
def solution(price, money, count):
    return max(0, price*(count+1)*count//2-money)