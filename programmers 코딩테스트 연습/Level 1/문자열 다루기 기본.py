def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False


# 좋아요 순
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)