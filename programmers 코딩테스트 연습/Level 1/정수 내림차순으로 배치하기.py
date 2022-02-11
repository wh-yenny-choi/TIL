def solution(n):
    n = sorted(str(n), reverse=True)
    return int(''.join(n))

# 좋아요 순
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));
'''
list로 감싸지 않아도 됩니다!! - 맞아요 sorted하면 리스트로 반환해서 나와요
'''

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))