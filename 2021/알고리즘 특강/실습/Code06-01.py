## 크기가 5칸인 스택의 생성과 데이터 3개 입력

stack = [None for _ in range(5)]  # stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print(stack)
print('-----스택 상태-----')
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

# pop
print('-----pop-----')
print('현재 스택 상태 -> \n', stack)
print('\n')

data = stack[top]
stack[top] = None
top -= 1
print(stack)
print('추출된것 :', data)

data = stack[top]
stack[top] = None
top -= 1
print(stack)
print('추출된것 :', data)

data = stack[top]
stack[top] = None
top -= 1
print(stack)
print('추출된것 :', data)
