# 곱하기 혹은 더하기
'''
문자열 s, + 혹은 x를 이용하여 가장 큰 수 구하기, 왼쪽부터 순서대로 이루어진다
02984
0이나 1이면 더하기 2부터 9까지 곱하기 이용
'''
s = input()
first = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or first <= 1:
        first += num
    else:
        first *= num
    result = first

print(result)