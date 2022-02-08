# 파이썬 진수 변환

### n진수 → 10진수

`int(string, base)`

- 결과값은 모두 string
- base에 진법 넣기



### 10진수 → 2, 8, 16 진수

`bin()` : 2진수 

`oct()` : 8진수

`hex()` : 16진수

````python
>>> print(bin(11))
0b1011
>>> print(oct(11))
0o13
>>> print(hex(11))
0xb
````

````python
# 진법 표시 지우기
>>> print(bin(11)[2:])
1011
>>> print(oct(11)[2:])
13
>>> print(hex(11)[2:])
b
````



### 10진수 → n 진수

> 코드 작성 필요

```python
def solution(n, q):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]  # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
```



### n진수 → n진수

-  <mark>n진수를 10진수로 변경하고 다시 n진수로 변경</mark>

````python
solution(int('c', 16), 4)  # 16진수 'c' → 4진수
solution(int('4', 6), 3)  # 6진수 '4' → 3진수
solution(int('21', 3), 7)  # 3진수 '21' → 7진수
solution(int('15', 9), 5)  # 9진수 '15' → 5진수
````



**Ex) 3진법 뒤집기**

````python
def solution(n):
    answer = ''
    
    while n > 0:
        n, mod = divmod(n, 3)  # 10진수 → 3진수
        answer += str(mod)
    
    return int(answer, 3)  # 3진수 'answer' → 10진수
````

[출처]

https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
