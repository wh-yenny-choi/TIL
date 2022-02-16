# 오답
def solution(s):
    if s[:1] == '(' and s[-1:] == ')':
        return True
    else:
        return False

# 2차 오답
def solution(s):
    if s[:1] == '(' and s[-1:] == ')':
        if s.count('(') != s.count(')'):
            return False
        return True

    else:
        return False
'''
() ) () ( (), false
구글링 도움
'''
count = 0
for i in s:
    if i == '(':
        k += 1
    elif i == ')':
        k -= 1
    if k < 0:
        return False

# 정답
def solution(s):
    if s[:1] == '(' and s[-1:] == ')':
        if s.count('(') != s.count(')'):
            return False
        # () ) () ( (), false
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            if count < 0:
                return False
        return True

    else:
        return False


# 좋아요 순 ternary operator
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

if i == '(':
    x += 1
else:
    x - 1
if i == ')':
    x += 1
else:
    x