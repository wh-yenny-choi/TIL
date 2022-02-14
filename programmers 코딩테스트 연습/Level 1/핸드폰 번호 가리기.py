# 1개 런타임 에러
def solution(phone_number):
    # phone_number-4까지 *, 그후 숫자
    if phone_number[:-4]:
        answer = '*' * len(phone_number[:-4])
    if phone_number[-4:]:
        answer += phone_number[-4:]
    return answer

# if문 안돌리고, answer만 사용해도 정답처리
def solution(phone_number):
    answer = '*' * len(phone_number[:-4])  # 마지막 4개 전까지 *
    answer += phone_number[-4:]
    return answer

# 좋아요 순
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

def solution(phone_number):
    return '*' * len(phone_number[:-4]) + phone_number[-4:]
'''
문자열도 곱셈, 덧셈 가능
'''