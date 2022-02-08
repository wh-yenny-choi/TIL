# Writing your first Django app

간단한 설문조사(Polls)어플리케이션 만드는 과정

## 프로젝트 뼈대 만들기

코딩은 프로젝트 뼈대를 만드는 것 부터 시작한다. 즉, 프레적트에 필요한 디렉토리 및 파일을 구성하고, 설정 파일을 setting한다. 그 외에도 기본 테이블을 생성하고, 관리자 계정인 super user를 생성하는 것이 필요하다. 프로젝트가 만들어지면 그 하위에 애플리케이션 디렉토리 및 파일을 구성

Django는 이런 작업을 위한 **Django Shell Command** 제공

![img](https://camo.githubusercontent.com/1223e7fa2f825ca50c946547f6f1a5557070a0b0a65d71c7737d770e392aeab7/68747470733a2f2f626c6f6766696c65732e707374617469632e6e65742f4d6a41784f5441794d4468664d6a49672f4d4441784e5451354e6a45784d5449314d7a6b302e7961715f324e2d4d4c71512d516753746330555a64305f7838364b415a56426b6b3762466b687238533730672e2d754c6c61466d4177734b336b5630627142502d38355258315f654f6c4841515577384f6647314f5f5449672e4a5045472e6a6a7363616e2f312e4a5047)

![img](https://camo.githubusercontent.com/19f6ea7de1b01487a768af570d046603bf583a34971d0cadb4b4be14c72352bc/68747470733a2f2f626c6f6766696c65732e707374617469632e6e65742f4d6a41784f5441794d4468664d5463342f4d4441784e5451354e6a45784e7a49354f544d322e736d6c2d426e4842356e2d7272656545586c49344a6350626d5a7431383642595236356131664c37416834672e616872705f3065706b563361763745357a356155335956355357686f6634586f304d73776544344a6b5341672e4a5045472e6a6a7363616e2f332e4a5047)

이 외에도 프레젝트가 완성된 후에 template, static, logs 등의 디렉토리가 더 필요하다. 프로젝트 개발을 진행하면서 임의로 추가해도 무방하다.

```django
django-admin startproject mysite // mysite라는 프로젝트를 생성함
python manage.py startapp polls // polls라는 애플리케이션을 생성함
notepad settings.py // 설정 파일을 확인 및 수정함
python manage.py migrate // 데이터베이스에 기본 테이블을 생성함
python manage.py runserver // 현재까지 작업을 개발용 웹 서버로 확인함
```

https://github.com/jjscan/md-docs/blob/master/%5B%EC%BD%94%EB%93%9C%EB%A6%AC%EB%B7%B0-4%5DDjango%20%EC%9B%B9%20%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC.md

## part1

#### 프로젝트 만들기 

- django -admin startproject '새로운 디렉토리'

#### 개발 서버

- 새로운 디렉토리로 이동
- python mange.py runserver
- runserver실행 오류시 환경 변수 변경
  - 시스템 환경 변수 편집 - 환경 변수 - 사용자 변수 - Path선택 - 편집 - 새로만들기
  - C:\Users\사용자명\Anaconda3
  - C:\Users\사용자명\Anaconda3\Scripts
  - C:\Users\사용자명\Anaconda3\Library\bin
  - C:\Users\사용자명\Anaconda3\Library\mingw-w64\bin
  - C:\Users\사용자명\Anaconda3\Library\usr\bin
  - 위의 4개 추가

#### 설문조사 앱 만들기

- 작업 시작을 위한 환경(프로젝트) 설치 완료
- polls 디렉토리 생성
- 첫번째 뷰 작성

**request와 response의 기본 흐름 이해과정**

https://docs.djangoproject.com/ko/3.2/intro/tutorial01/



## part2

#### 데이터 베이스 설치

- 데이터베이스에서 테이블 미리 만들기
- python mange.pyh migrate

#### 모델 만들기

- 모델: 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말한다.
- Django는 DRY원칙에 따라 데이터 모델을 한곳에서 정의하고, 이것으로부터 자동으로 뭔가를 유도하는 것이 목표
  - 반복하지 말 것(DRY) : 고유한 개념 및 데이터는 단 한 번, 단 한 곳에 존재하는 것으로 족하다. 반복성은 bad, 정규화는 good. 최소한의 것들을 가지고 최대한의 것을 만들어 내도록 하는 원칙

#### 모델의 활성화

- 모델에 대한 코드로 Django에게 정보 전달. Django는 이 정보를 가지고 다음과 같은 작업 수행 가능
  - 이 앱을 위한 데이터베이스 스키마 생성(create table문)
  - 객체에 접근하기 위한 Python 데이터베이스 접급 API를 생성
- python manage.py makemigrations polls
  - makemigrations을 실행시킴으로서, 모델 변경 사실과 이 변경사항을 migration으로 저장시키고 싶다는 것을 Django에 알림
- python manage.py sqlmigrate polls 0001
  - migrate : migration실행, 자동으로 데이터베이스 스키마를 관리하게 해주는 명령어
  - sqlmigration : migration이름을 인수로 받아 실행하는 SQL문장 보여줌 (migtation이 내부적으로 어떤 SQL문장을 실행하는지)

#### API 가지고 놀기

- 대화식 Python 쉘(shell)에서 Django (DB)API 사용

- Python shell 실행

  - python manage.py shell

- Exception [WinError 995] 스레드 종료 또는 응용 프로그램 요청 때문에 I/O 작업이 취소되었습니다

  - 파이썬 3.8버전에서 위와같은 오류 발생시 prompt-toolkit 패키지를 다운그레이드해야한다.

  - ```
    pip install --upgrade prompt-toolkit==2.0.10
    ```

https://docs.djangoproject.com/ko/3.2/intro/tutorial02/



## part3

#### 뷰 추가하기

- 인수를 받는 뷰를 추가 (def ···)
- path() 호출 추가하여 새로운 뷰를 urls 모듈로 연결
  - path() 함수에는 2개의 필수 인수 : route, view / 2개의 선택 인수 : kwargs, name까지 총 4개 인수전달. 아래는 path()인수들 설명
    - route : URL 패턴을 가진 문자열. 요청 처리시, Django는 urlpatterns의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL을 각 패턴과 리스트의 순서대로 비교. 패턴들은 GET이나 POST의 매개 변수들, 혹은 도메일 이름 검색하지 않는다. 
      - ex) http://127.0.0.1:8000/polls/5/results/이 요청된 경우 URLconf는 오직 polls/부분만 신경쓴다.
    - view : Django에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 <캡처된>값을 키워드 인수로 하여 특정한 view함수를 호출
    - kwargs : 임의의 키워드 인수들은 목표한 view에 사전형으로 전달
    - name : URL에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있다. 단 하나의 파일만 수정해도 project내의 모든 URL패턴을 바꿀 수 있도록 도와준다.

#### 뷰가 실제로 뭔가를 하도록 만들기

- 각 뷰는 두가지 중 하나를 하도록 되어있다.
  1. 요청된 페이지의 내용이 담긴 HttpResponse 객체 반환
  2. Http404 같은 예외 발생하게 해야한다.
- Django에 필요한 것은 HttpResponse 객체 혹은 예외
- Django 자체 데이터베이스 API를 사용하기

지름길 : render()

- 템플릿에 context를 채워넣어 표현한 결과를 HttpResponse객체와 함께 돌려주는 구문은 자주 쓰는 용법이다. 따라서 Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능(shortcuts)을 제공한다. 

- ```django
  from django.shortcuts import render
  ```



#### 404에러 일으키기

질문의 상세 뷰에 태클걸어, 뷰는 요청된 질문의 ID가 없는 경우 **Http404** 예외 발생 시킨다.

**지름길 : get_object_or_404()**

- 만약 객체가 존재하지 않을때 **get()**을 사용하여 **Http404** 예외를 발생시키는 것은 자주 쓰이는 용법이다.
-  **get_object_or_404()** 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 **get()**함수에 넘긴다. 만약 객체가 존재하지 않을 때, Http404 예외 발생

https://docs.djangoproject.com/ko/3.2/intro/tutorial03/

