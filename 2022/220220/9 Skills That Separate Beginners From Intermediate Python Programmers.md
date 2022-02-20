### 9 Skills That Separate Beginners From Intermediate Python Programmers

> Thinking and writing code…but mostly thinking



#### Beginner vs. Intermediate

- Problem-solving and asking questions. (문제해결과 질문)
- The XY Problem
- Understanding why the code works (or doesn’t) (어떻게 코드가 작동하는지에 대한 이해)
- Working with strings 
- Working with lists
- Using loops
- Using functions (and talking about them correctly).
- Object-Oriented Programming (객체지향 프로그래밍)
- Respect PEP



##### 1. Problem-Solving and Asking Questions

프로그래밍은 단순히 코드를 작성하는 것이 아니다. 문제 해결이 초보를 벗어나기위한 중요한 스킬이다.

문제를 질문하는 것은 물론 중요하다. 하지만 코드 구현에 어려움이 있다고 혼자서 생각하는 시간도 없이 아무런 노력을 하지 않고 정답 코드만을 본다면 아무것도 배울 수 없다.



##### 2. The XY Problem

X라는 문제가 있을때, X에 대한 해답을 구해야지 Y에 대한 해답을 구하면 안된다.

즉, 문제를 제대로 이해하고 일회성 답이 아닌 전체적으로 봤을때 작동되는 로직을 구현해야 한다.

**EX) 파일 확장자 추출하기**

```python
# 끝의 3자리 추출하면 되겠다!
def extract_ext(filename):
    return filename[-3:]
print (extract_ext('photo_of_sasquatch.png'))
>>> png

# 만약 photo_of_lochness.jpeg라면 작동하지 않는다
# 제대로 된 코드
def extract_ext(filename):
    return filename.split('.')[-1]
print (extract_ext('photo_of_sasquatch.png'))
print (extract_ext('photo_of_lochness.jpeg'))
>>> png
>>> jpeg
```

확장자를 추출하고 싶다면, 확장자를 추출하는 코드를 제대로 짜야한다.



##### 3. Understanding Why the Code Works (Or Doesn’t)

기도메타로 짠 코드가 정답처리가 된다고 해서 바로 다음 단계로 넘어가는 행동이야말로 최악의 행동 중 하나이다.

코드가 어느 부분에서 에러가 나는지 모르는것은 위험하다. 하지만, 정답 처리가 된 코드를 제대로 이해하지 않고 넘어가는것은 더 위험하다.

코드 에러가 나고 어느부분을 해결해야하는지 모르는 경우는 흔하다. 여기서 중요한 것은, trobleshoot을 하고 나서 정리하고 왜 에러가 났는지 이해하고 넘어가는 것이다. 

이것이 한 단계 성장할 수 있는 자산이 될 것이다.



##### 4. Working With Strings

string뿐 아니라 전체적인 library를 살펴볼 필요가 있다.

string은 원소들의 리스트로서 보여질 수 있고, index를 이용하여 string의 원소를 이용할 수 있다.

str()를 어떻게 이용하는지는 모두가 안다. 초보를 벗어나고 싶다면 str() 문서를 살펴봐야 한다. 

- help(str) 또는 dir(str) 작성하면 확인 가능

그렇다면 endswith()라는 함수를 확인할 수 있다. 이를 이용하면 1번의 문제를 다른 방식으로 해결할 수 있다.

```python
# 파일의 타입 알아내기
filenames = ['lochness.png' , 'e.t.jpeg' , 'conspiracy_theories_CONFIRMED.zip']

# 1: Using ENDSWITH
for files in filenames:
    if files.endswith('zip'):
        print(f'{files} is a zip file')
    else:
        print (f'{files} is NOT a zip file')

# 2: Using SPLIT (1번과 동일한 해결 방법)
for files in filenames:
    if files.split('.')[-1] == 'zip':
        print(f'{files} is a zip file (using split)')
    else:
        print (f'{files} is NOT a zip file (using split)')
```



##### 5. Working With Lists

List는 다방면으로 활용 가능하다.

여기 int형과 string형이 뒤죽박죽인 리스트가 있다.

```python
my_list = ['a' , 'b' , 'n' , 'x' , 1 , 2 , 3, 'a' , 'n' , 'b']
for item in my_list:
    print (f'current item: {item}, Type: {type(item)}')
```

int형과 string형을 구분하려고 시도할 때, 반복문을 사용하여 list내의 원소를 하나씩 확인하는 것이 하나의 방법일 것이다. 초보자들은 이런 반복문을 주로 사용한다.

```python
my_list = ['a' , 'b' , 'n' , 'x' , 1 , 2 , 3 , 'a' , 33.3 , 'n' , 'b']
number_list = []
string_list = []
for item in my_list:
    print (f'current item: {item}, Type: {type(item)}')
    if not isinstance(item,str):
        number_list.append(item)
    else:
        string_list.append(item)
my_list = string_list
```

좀 지저분하지만 작동하는 코드이다. 하지만 list comprehensions을 배워서 사용할 수 있다면 한줄로 표현 가능하다.

```python
my_list = [letter for letter in my_list if isinstance(letter,str)]
```

filter함수를 이용한다면?

```python
def get_numbers(input_char):
    if not isinstance(input_char,str):
        return True
    return False

my_list = [1,2,3,'a','b','c']
check_list = filter(get_numbers, my_list)
for items in check_list:
    print(items)
```

문제를 해결하기 위한 답은 정말 다양하게 존재할 수 있다. 상황에 맞는 최선을 답을 찾아내야한다.

**보너스**

- list나 string 역순 출력하는 법

```python
names = ['First' , 'Middle' , 'Last']
print(names[::-1])
>>> ['Last', 'Middle', 'First']
```

- list내 원소들 join하는 법

```python
names = ['First' , 'Middle' , 'Last']
full_name = ' '.join(names)
print(f'Full Name:\n{full_name}')
>>> First Middle Last
```



- isinstance(확인하고자 하는 데이터 값, 확인하고자 하는 데이터 타입)
  - isinstance(인스턴스, 데이터나 클래스 타입)

```python
# 정수인지 확인 
result1 = isinstance(100, int) 
print(f'isinstance(100, int) : {result1}') 
>> True

# 실수인지 확인 
result2 = isinstance(100, float) print(f'isinstance(100, float) : {result2}') 
>> False

# 문자열인지 확인 
result3 = isinstance('BlockDMask', str) print(f'isinstance("BlockDMask", str) : {result3}') 
>> True

# 리스트인지 확인 
result4 = isinstance([1,2,3], list) print(f'isinstance([1,2,3], list) : {result4}')
>> Ture
```



- filter()내장함수는 여러 개의 데이터로 부터 일부의 데이터만 추려낼 때 사용

  - 주로 list, tuple대상으로 사용

  - filter(조건 함수, 순회 가능한 데이터)
  - 두번째 인자로 넘어온 데이터 중 첫번째 인자로 넘어온 조건 함수를 만족하는 데이터만을 반환

```python
>>> users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
...  {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
...  {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
...  {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
...  {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

>>> def is_man(user):
...     return user["sex"] == "M"

>>> for man in filter(is_man, users):
...     print(man)
...
{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'}
{'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'}
```



##### 6. Using Loops

파이썬 장점을 이용해서 코드 짤 수 있다.

```python
greek_gods = ['Zeus' , 'Hera' , 'Poseidon' , 'Apollo' , 'Bob']

for index in range(0,len(greek_gods)):
    print (f'at index {index} , we have : {greek_gods[index]}')

# 좀더 파이썬틱
for name in greek_gods:
    print (f'Greek God: {name}')
```

index와 함께 출력하고 싶다면 enumerate() 함수 이용

```python
for index, name in enumerate(greek_gods):
    print (f'at index {index} , we have : {name}')
```



##### 7. Using Functions (and talking about them correctly)

함수를 잘 이용하면 시간을 훨씬 절약할 수 있다. 같은 동작을 반복한다면 프로시저나 함수을 고려해야한다.

함수는 무언가를 **return**하고, 프로시저는 **print**한다.

- 함수는 반환값이 있고, 프로시저는 반환값이 없다.

parameters(매개변수) vs. arguments(인자)

- 프로시저나 함수에서 정의하는것이 매개변수
- 결과값으로 나오는것이 인자

```python
# procedure
def print_name(name)  # name : 매개변수
	print(name)
    
# function
def return_name(name)  # name :매개변수
	return(name)

print_name('Martin')  # Martin : 인자
>>> Martin
return_name('Martin')  # Martin : 인자
>>>
print(return_name('Martin'))  # Martin : 인자
>>> Martin
```

반복되는 코드 대신 프로시저를 사용한 예시

```python
def print_list(input_list):
    for each in input_list:
        print(f'{each}')
    print() #just to separate output
greek_gods = ['Zeus' , 'Hera' , 'Poseidon' , 'Apollo' , 'Bob']
grocery_list = ['Apples' , 'Milk' , 'Bread']
print_list(greek_gods)
print_list(grocery_list)
print_list(['a' , 'b' , 'c'])

# 역순 출력
def reverse_list(list_input):
    return list_input[::-1]
my_list = ['a', 'b' , 'c']
print (reverse_list(my_list))
>>> ['c', 'b', 'a']
```



##### 8. Object-Oriented Programming

파이썬은 객체지향 언어이고, 객체가 파이썬의 최장점이다. 객체가 설계도라고 생각할 때, 설계도를 이용하면 인스턴스를 만들 수 있다

student 클래스를 예시로 들자. student클래스에는 name와 subject_list가 있다.

```python
class Student():
    def __init__(self,name):
        self._name = name
        self._subject_list = []
```

__ init __ 는 클래스의 생성자이다. 이곳에 클래스 핵심 내용이 들어간다. 

학생을 생성하고 싶다면, 변수에 다음과 같이 할당할 수 있다.

```python
student1 = Student('Martin Aaberge')
student2 = Student('Ninja Henderson')
```

student클래스에는 student1, student2 인스턴스가 존재하게 되었다. 두개의 인스턴스는 모두 같은 설계도를 공유하지만, 그뿐이다. 여기서 student클래스에 딱히 할건 없지만 subject_list를 추가해볼 수는 있다. 메소드를 만들고, 클래스의 인스턴스와 상호작용하도록 할 수 있다.

```python
class Student():
    def __init__(self,name):
        self._name = name
        self._subject_list = []
    def add_subject(self, subject_name):
        self._subject_list.append(subject_name)
    def get_student_data(self):
        print (f'Student: {self._name} is assigned to:')
        for subject in self._subject_list:
            print (f'{subject}')
        print()
```

student클래스에 저장한 정보를 얻거나, 학생을 추가하거나, 학생 정보를 편집할 수 있다.

```python
#create students:
student1 = Student('Martin Aaberge')
student2 = Student('Heidi Hummelvold')

#add subjects to student1
student1.add_subject('psychology_101')
student1.add_subject('it_security_101')

#add subject to student2
student2.add_subject('leadership_101')

#print current data on students
student1.get_student_data()
student2.get_student_data()
```

class student()를 정의한 student.py파일을 main.py로 import 가능하다. (이 경우 모든 파일은 같은 위치에 존재해야 한다.)

```python
from student import Studentstudent1 = Student('Martin')
student1.add_subject('biomechanics_2020')
student1.get_student_data()
```



##### 9. Respect PEP

PEP를 생각하지 않고 코드를 작성하는 사람을 종종 목격한다. 

PEP기준이 아니더라도, 개발 환경에서는 각 상황의 기준을 따르는것이 중요하다. 

PEP는 코드에 관한 가이드라인의 집합이다. PEP-8 읽어보면 도움이 될 것이다. https://www.python.org/dev/peps/pep-0008/

쉽게 말하면 snake_case를 예시로 들 수 있다. 파이썬에서 변수 선언을 할때는 _(underscore)를 이용하여 문자를 구분해야 한다.

```python
chocolateCake = 'Yummy'
# 가 아니라
chocolate_cake = 'yummy'
```



**출처**

https://betterprogramming.pub/9-skills-that-separate-a-beginner-from-an-intermediate-python-programmer-8bbde735c246