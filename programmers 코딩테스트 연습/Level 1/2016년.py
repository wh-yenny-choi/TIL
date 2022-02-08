# 구글링했음
def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = days * 55
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = days[sum(months[:a]) + b - 1]
    return answer
