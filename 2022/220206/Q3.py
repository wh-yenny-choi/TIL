# 문자열 뒤집기
'''
문자열 s,

'''
s = input()
turn0to1 = 0
turn1to0 = 0

if s[0] == '0':
    turn0to1 += 1
else:
    turn1to0 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            turn1to0 += 1
        else:
            turn0to1 += 1

result = min(turn0to1, turn1to0)

print(result)
