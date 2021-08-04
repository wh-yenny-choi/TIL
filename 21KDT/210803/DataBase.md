# DATA BASE (DB)

## 차례

DATA BASE의 정의와 태동

DATA BASE의 역사

DATA와 정보

DATA와 지식과의 관계

DATA의 종류

DATA의 생성속도

DATA 분석 적용 사례

스프레드시트와 DATABASE 차이

SQL 이란?

데이터베이스 객체란?

데이터베이스 객체의 종류

DATA BASE 기출 문제 예시

DATA BASE (SQL 기본쿼리 구조)

SQL 문장의 종류

ACID?

DATA BASE Table이란?

스키마 다이어그램

SELECT와 FROM절

WHERE절과 filtering

변수의 사용

ORDER BY절

SQL JOIN

SQL Sub queries

CREATE TABLE

SQL Inserting, Updating and Deleting

SQL Constraints 실습

INDEX란?

MS EXPRESS의 설치



## DATA BASE의 정의와 태동

다수의 사람들에게 공유되고, 사용될 목적으로 통합/관리되는 데이터의 집합

- 자료항목의 중복을 없애고 자료를 구조화하여 저장하므로써 검색 성능을 높인다.
- 데이터베이스에 대한 검색, 삽입, 변경, 삭제등의 주요 작업등이 있으며
- 자료 검색과 갱신의 효율을 높인다.
- 현대적 의미의 데이터베이스 개념은 1960년대부터 시작하였다.



**B+ Tree Index**

Index 길이가 0~100 일때,

1. 가운데를 자른다 (50 : 50)
2. 50에서 가운데를 자른다. (25:25:25:25)
3. 반복



## DATA와 정보

데이터 (data) 

- 세상으로부터 관찰된 내용이나 측정 등의 수단을 통하여 수집한 사실이나 값

정보 (information)

- 데이터 가공 결과
- 특정 상황에 대한 의사 결정을 내릴 수 있는 유용한 해석 또는 데이터 상호간의 관계 파악



## DATA와 지식과의 관계

지식(knowledge)

- 사람이 정보를 처리하고 연관 짓는 구조 또는 컴퓨터 체계가 명백한 방식으로 행동하기 위하여 갖추어야 할 정보를 형성하는 규칙 또는 환경

의사결정(Decision)

- 목표를 달성하기 위한 대안 중 가장 효율적인 방안을 선택



## DATA의 종류

정형데이터 : RDBMS, 스프레드시트

반정형데이터 : XML, HTML(스키마 포함)

비정형데이터 : 분석가능한 text, image, 동영상, 음성데이터



## DATA의 생성속도

하루 <u>250경</u> 바이트 비정형 정보

매달 <u>10억</u> 여 개 트윗

매달 <u>300억</u> 여 개 페이스북 메세지

<u>1조</u> 대 이상 모바일 기기로 가속화



## DATA 분석 적용 사례

X축 : **데이터 속도**

- 데이터 속도 빠르면, **실시간**
- 데이터 속도 느리면, **배치처리**

Y축 : **데이터의 다양성**

- 다양성 적으면, **정형데이터**
- 다양성 중간, **반정형데이터**
- 다양성 높으면, **비정형데이터**



## 스프레드시트와 DATABASE 차이

스프레드 시트

- 1980년대 초 personal computer 등장과 함께 환영받는 프로그램이었으며, 워드프로세서 다음으로 많이 사용되는 tool이었다.
- 심폰, 로터스 1-2-3등 여러 형태의 스프레드시트가 존재하였으나, 
- 현재에는 Microsoft Excel이 전세계에서 대부분 사용되고 있다.

DATABASE

- Database는 Host컴퓨터로부터 사용되어져 왔는데, 
- 현재에는 IT산업의 쌀이라 불리우며,대부분의 기업에서 
- 정보 저장 및 분석, 활용을 활발히 하는 data의 집합체이다.
- 과거에는 정형데이터의 저장이 일반적이였으나,
- 현재에는 big data의 개념이 중요해짐에 따라
- 비정형 데이터의 형태도 저장, 관리되고 있다.



## SQL 이란?

Structured Query Language

SQL ↔ Database

- 데이터베이스를 구축하고 활용하기 위해 사용하는 언어
- SQL은 관계형 데이터 모델로 표현되는 DB를 조작하는 언어로 초기 IBM에서 상용화 함
- SQL언어가 가장 널리 사용되고 있는 이유는 미국 국립 표준 협회가 이를 표준으로 제정함
- SQL은 영어 문장 형태로 일반 사용자도 쉽게 사용

ANSI

SQL-86

SQL-89

SQL-92

SQL:1999

SQL:2003

SQL:2006

SQL:2008

SQL:2011



## 데이터베이스 객체란?

데이터베이스에 저장되는 요소 중 테이블과 여러가지 요소들이 저장 됨

이것을 데이터베이스 객체(Database Objects)라고 명명 함

- **테이블**, **인덱스**, 종속관계(constraints), View, Trigger 등 여러가지 요소가 저장



> 인간의 말을 컴퓨터 언어로?

- 파싱 (parse)
  - DB에서의 용어
  - 파싱하다 = 문법적 해부 
  - 주로 다른 언어로 작성된 문서를 디코딩 한다는 의미로 해석할 수 있다
- 컴파일
  - 컴파일하다 = 기계어 번역
- 인코딩



> 컴퓨팅 파워가 좋다는 말이 varchar을 쓴다는 것과 어떻게 연결이 되는지 자세히 설명해 주실 수 있을까요?

- 컴퓨팅 파워가 좋다 = 컴퓨터가 일을 잘한다 = 컴퓨팅 성능이 좋다 
  - ⇒ 계산 능력이 좋다, 처리 능력이 좋다, 빠르다
  - 예를 들어 데스크탑은 노트북에 비해 컴퓨팅 파워가 좋다

- 넉넉한 varchar size 사용 가능



> 컴퓨터를 종료해도 시간이 계속 업데이트 되는 이유?

- CMOS  / BIOS
  -  System Time 정의





## 데이터베이스 객체의 종류

**테이블 (Table)** : 데이터 저장 공간

- 하나 또는 여러 컬럼들이 모여 하나의 레코드를 구성 함

- 여러 레코드들이 모여 다시 테이블이 됨

  - 환자 테이블은 환자번호, 성명, 진료과목 등 여러 컬럼을 갖게 되며 환자수만큼의 레코드를 갖게 됨

- 시스템 테이블의 경우, 대부분 SQL Server가 내부적으로 관리를 목적으로 사용하게 됨

- 일반 사용자의 경우, 사용자 테이블을 대부분 사용하게 되며, 시스템 테이블의 접근 보다는 저장프로시저나 스키마뷰를 이용해서 이러한 정보를 참조할 수 있음

  

**인덱스 (Index)** : 테이블에 있는 데이터를 빠르게 검색 위한 객체

- 쿼리문을 이용하여 정보를 검색할 때 빠른 수행을 위해서 인덱스를 구성하여 사용 됨
- 다른 목적으로는 데이터의 무결성을 위해서도 사용
- SQL Server의 경우 Clustered 인덱스, Non Clustered 인덱스 등 두가지로 사용 됨
- 데이터베이스가 유용한 점은 Index의 사용이 최대 장점이라 할 수 있음



**View** : 실제로는 존재하지 않는 가상의 테이블

- 실제 테이블을 사용자 입장에서 논리적인 테이블을 만들어 쉽게 접근 할 수 있게 함
- 사용 목적은 편리성과 보안성



**Stored Procedure** : DB 내부에 저장된 일련의 SQL 명령문들을 하나의 함수처럼 실행하기 위한 쿼리의 집합

- 쿼리문을 저장해 두었다가 손쉽게 재사용할 수 있는 저장 프로시저
- 저장 프로시저가 생성이 되면, 소스 프로시저가 최초 한 번 컴파일 된 후, 처음 수행될 때만 한 번 만들어지고
- 이후에는 이러한 과정이 생략되고 컴파일 된 형태를 그대로 재사용하기 때문에 일반적인 쿼리수행에 비해 빠른 성능을 제공



**Trigger** : 이벤트(삽입, 삭제, 갱신 등) 발생시 자동화 작업 수행

- 테이블의 값이 변경(insert, update, delete)될 때 자동으로 수행되는 저장 프로시저
- 방아쇠를 당긴다는 의미로, 미리 정의된 프로시저 안에서 자동으로 수행되는 프로시저



**Data Type** : 실수치, 정수, 불린 자료형 따위의 여러 종류의 데이터를 식별하는 분류로서, 더 나아가 해당 자료형에 대한 가능한 값, 해당 자료형에서 수행을 마칠 수 있는 명령들, 데이터의 의미, 해당 자료형의 값을 저장하는 방식을 결정한다

- SQL Server가 제공하는 기본적인 데이터 형식말고도 User defined 데이터 형식
  - 환자 이름을 선언하는 데 있어 어느 사용자는 CHAR, VARCHAR 등 다르게 사용할 수 있는데, 데이터 타입을 통일시켜 사용하기 위하여 HWNJA_TYPE 이라는 데이터 형식을 만들어 선언하면, 
  - 사용자들은 환자 이름의 데이터 형식을 HWANJA_TYPE이라고 지정해서 사용



**Default** : 응용 소프트웨어나 컴퓨터 프로그램, 또는 장치에서 사용자의 개입없이 자동으로 할당되는 설정 또는 값

- 데이터가 입력될 때 값이 들어오지 않으면 자동으로 입력되도록 디폴트를 지정할 수 있음
  - 최초 진료일이 없을 경우, 자동으로 오늘 날짜가 입력 되도록 지정 할 수 있음



**Rule** : 특정 컬럼에 대하여 저장될 수 있는 값을 지정할 때 사용



**Constraint **(종속관계) : 테이블과 테이블 간의 relationship(연결관계)  

- 데이터의 무결성을 위해 사용
- Primary Key, Foreign Key, Check 등



## DATA BASE (SQL 기본쿼리 구조)

```sql
SELECT 필드명1, 필드명2,...,필드명n
FROM 테이블 명
WHERE 조건
GROUP BY 필드명
HAVING 조건
ORDER BY 필드명 (ASC|DESC)
```

 

**기본 구조**

```sql
# 단순 SELECT 문장
SELECT * FROM 사원;	

# 필드명 변경 후 SELECT한 문장
SELECT 사원번호, 성, 이름, 직급 AS 현재타이틀 

# SELECT에 조건문을 주어 검색(WHERE절)
SELECT 사원번호, 성, 이름, 직급 AS 현재타이틀 
FROM 사원
WHERE 직급 = '과장';

# SELECT에 조건문을 주어 검색(WERE절)
SELECT 사원번호, 성, 이름, 직급 AS 현재타이틀, 근무시작일 
FROM 사원
WHERE 근무시작일 > '20000101' AND 근무시작일 < '20021231';

# ORDER BY절 (ASC|DESE)
SELECT 사원번호, 성, 이름, 직급 AS 현재타이틀, 근무시작일
FROM 사원
ORDER BY 성(ASC);  # ASC는 생략 가능  

# GROUP BY 절 
SELECT 시도, COUNT(*) 사원번호
FROM 사원
GROUP BY 시도;

# HAVING 절
SELECT 시도, COUNT(*) 사원번호
FROM 사원
GROUP BY 시도
HAVING COUNT(*) >= 2;

# SELECT + FROM + GROUP BY + HAVING + ORDER BY
SELECT 시도, COUNT(*) 사원번호
FROM 사원
GROUP BY 시도
HAVING COUNT(*) >= 1
ORDER BY 1;
```



**WHERE 절 조건식**

연산자 종류

- 일반 연산자 : `+` `-`  `*` `/`
- 비교 연산자 : `=` `<>` `>` `<` `>=` `<=`
- 논리 연산자 : `AND` `OR` `NOT`
- 특수 연산자 : `BETWEEN` `IN`
- LIKE 연산자 : `*` `%`
- NULL 연산자 : `IS NOT NULL` `NULL`

우선순위 

- () → 논리 연산자 제외한 연산자 → NOT → AND → OR 
- NULL 은 어떤값이 입력 될지 모른다.

> ##### 애스터리스크 (*asterisk*, 별표) : 곱하기 표시할 때, 알파벳 X와 혼동되는 것을 방지하기 위해 * 사용



**논리게이트**

OR (+)

| X    | Y    | F    |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 0    | 1    | 1    |
| 1    | 0    | 1    |
| 1    | 1    | 1    |



AND (*)

| X    | Y    | F    |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 0    | 1    | 0    |
| 1    | 0    | 0    |
| 1    | 1    | 1    |



NOR (OR의 반대 = + 의 반대)

| X    | Y    | F    |
| ---- | ---- | ---- |
| 0    | 0    | 1    |
| 0    | 1    | 0    |
| 1    | 0    | 0    |
| 1    | 1    | 0    |



NAND (AND의 반대 = *의 반대)

| X    | Y    | F    |
| ---- | ---- | ---- |
| 0    | 0    | 1    |
| 0    | 1    | 1    |
| 1    | 0    | 1    |
| 1    | 1    | 0    |



**그룹함수의 종류**

SUM()

MAX()

MIN()

AVG()

COUNT()



### sql 문장 예시

**문제** 입사일이 2018년 1월부터 6월 까지이며, 연봉이 2000만원 미만인 사원명, 사원번호, 연봉 출력 (사원테이블 : emp)

**답**

select 사원명, 사원번호, 연봉 from emp where 입사일 between '20180101' and '20180630', 연봉 <2000;



## SQL 문장의 종류

SQL

- DDL : 데이터 정의어 (DB구조 정의, 생성, 삭제)
  - CREATE
  - ALTER
  - TRUNCATE
  - RENAME
  - DROP
- DML : 데이터 조작어 (데이터 삽입, 변경, 삭제)
  - INSERT
  - UPDATE
  - DELETE
- DRL : 데이터 질의어 (데이터 검색)
  - SELECT
- TCL : 트랜잭션 조정어 (트랜잭선 반영, 취소)
  - COMMIT
    - 트랜잭션 처리가 종료되어 변경 내용을 DB에 반영하는 명령어
  - ROLLBACK
    - 하나의 트랜잭션 처리가 비정상적으로 종료되었을 떄 모든 변경 작업을 취소하고 이전 상태로 되돌리는 연산
  - SAVEPOINT
    - ROLLBACK할 위치인 저장점을 지정하는 명령어 (maker 역할)
- DCL : 데이터 제어어 (사용권한 부여, 제거)
  - GRANT
  - REVOKE



> ##### 게임회사의 트랜잭션은 약 10억건



## ACID? 🌟

**원자성 (Atomicity)** 

- 트랜잭션 (일의 시작과 끝)과 관련된 작업들의 성공을 보장하는 능력
  - 예. ATM이체의 과정을 살펴보면 성공적인 과정인 경우, 현금인출의 경우 성공하면 원장에 자금이 가감되고 현금이 인출된다. 만약 현금이 일부 인출되고 원장에 가감된 금액이 기록된다면 실패이다.
- 이러한 일의 시작과 끝이 완료되도록 보장하는 것이다.

**일관성 (Consistency)**

- 트랜잭션이 commit(영구저장)되면, 데이터 일관성을 유지하여야 한다.
- 다른 트랜잭션이 동시에 commit된 데이터를 조작하려 할때 rollback(원위치)된다.
  - 먼저 commit선점시, 다른사람이 ownership을 가질 수 없다.

**고립성 (Isolation)**

- 트랜잭션의 수행 중 다른 트랜잭션이 방해하지 못하도록 하는 작업이다.
- 작업의 연속성을 확보할 수 있다. 장애요인이 될 수 있는데, 전체적 데이터베이스의 성능에 문제가 생길 수 있다.

**지속성 (Durability)**

- 완료된 트랜잭션은 데이터베이스에 영구 반영되어야 한다. 
- 데이터베이스 시스템의 관점에서 데이터의 보장을 의미한다. 
- 시스템의 문제시, 데이터베이스 차원에서 데이터의 redo, undo작업을 데이터베이스 로그에 기록함으로써 재해 또는 비정상적인 문제 발생시 데이터베이스 시스템 차원에서 대비하여 이를 보장할 수 있다.



> ##### NoSQL → ACID를 만족하지 않아도 됨  

네트워크 분할, 정전 등의 오류 시에도 데이터베이스 트랜잭션이 항시 제대로 수행되게 하려면 4가지 ACID 속성(원자성(A), 일관성(C), 고립성(I), 지속성(D))이 준수돼야 한다. 이 ACID 측면에서 단일 서버에 있는 데이터베이스는 ACID 속성을 전부 만족하기가 비교적 쉽다.

반면 분산 데이터베이스는 이행하기가 약간 더 까다롭다. NoSQL 데이터베이스는 '수평 확장성(Scale-Out, 다수의 서버에서 실행 가능하다는 의미)'의 장점이 있었지만 ACID 전체를 따르지 못하는 경우가 많았다.



## DATA BASE Table이란?

### DATA BASE Table이란? (1)

table(메타데이터)

- 데이터베이스에 대한 데이터를 의미함
- 데이터 구조나 제약사항 등과 같은 속성이나 특성을 기술하는 것

예시 ) 사원 Table

- 타임, 인스턴스, 속성, 도메인, 튜플

| 이름 | 학년 | 학번    | 학과 |
| ---- | ---- | ------- | ---- |
| 전   | 1    | 2014451 | 컴공 |
| 김   | 3    | 2011317 | 의료 |
| 박   | 2    | 2013586 | 의료 |
| 정   | 1    | 2015577 | 컴공 |

- 학번을 PK로 지정 후 학습
- 컴퓨터 위한 컬럼 베이스로 데이터베이스 저장
  - 사람은 로우 베이스를 더 선호



> ##### **서치 = 쿼리**



### DATA BASE Table이란? (2)

DDL문장으로 TABLE 생성, 변경, 삭제 가능

```sql
# TABLE 생성
CREATE TABLE 
#TABLE 변경	
ALTER TABLE 
# TABLE 삭제
DROP TABLE
```

예시

```sql
CREATE TABLE 학생
(
이름 varchar(10) NOT NULL,
이름 integer NOT NULL,
학번 integer NOT NULL,
학과 varchar(10) NOT NULL
);
```



> ##### char와 varchar 차이?

CHAR와 VARCHAR의 차이는 저장 영역과 문자열의 비교 방법이다

| 자료형  | 의미          | 대응하는 범위 |
| ------- | ------------- | ------------- |
| CHAR    | 고정형 문자열 | 255자까지     |
| VARCHAR | 가변형 문자열 | 1 ~ 65535     |

- 자료형 char와 varchar는 문자열을 표현할 때 사용하는 자료형으로 사용시 길이를 명시해 주어야 한다.
- 고정 사이즈인 char타입은 추후에 연산할 필요가 없기 때문에 검색속도 및 읽히는 속도가 다른 타입보다 빠르다. 사이즈 고정되어 있을때, char타입을 사용하면 더 효율적으로 데이터를 관리할 수 있다.
  - 예. 아이디, 주민등록번호...
- 가변 사이즈인 varchar은 이벽한 크기만큼의 공간만 잡힌다.
  - 예. varchar(20)인 경우, 2byte의 문자를 넣으면 2byte만큼의 데이터만 잡는다.
    - char(20)의 경우,  2byte의 문자를 넣으면 20byte만큼의 데이터를 잡는다.



> ##### 다른 데이터 타입?

- 정수형
  - byte, short, int, long
- 실수형
  - float, double
- 문자
  - char



### DATA BASE Table이란? (3)

DML문장으로 TABLE데이터 입력

```sql
INSERT INTO 테이블명 VALUES (···);	
```

예시

```sql
INSERT INTO 학생 VALUES ('전', 1, 2014451, '컴공');
INSERT INTO 학생 VALUES ('김', 3, 2011317, '의료');
INSERT INTO 학생 VALUES ('박', 2, 2013586, '의료');
INSERT INTO 학생 VALUES ('정', 1, 2015577, '컴공');
```



#### ROW ID

- ROW ID는 오라클에 국한되어 있음
- 각각의 row마다 DB가 부여한 row id의 고유 번호를 가지고 있음
- 로우아이디를 서치 ⇒ 인덱스

인덱스에는 row id 가 있음. 이 row id를 정렬시킨 것이 인덱스

- 인덱스 잘 정렬되어 있으므로 중간을 잘라서 크고 작은것을 판단 가능 ⇒ 빠르게 검색 가능



> ##### INSERT되는 순서가 뒤죽박죽이라면 문제가 될까?

ROW에는 해당하는 고유값을 가지고 있어서, 문제가 되지 않는다.

컴퓨터는 ROW값을 바라보고 있기 때문에 데이터베이스 내에만 있다면,

즉, address (ROW ID)만을 보고 처리하기 때문에 아무 문제 없음



### DATA BASE Table이란? (4)

DRL 문장으로 한 개의 학생을 검색

```sql
SELECT * FROM 학생 WHERE 이름 = '김소연';
```



### DATA BASE Table이란? (5)

DML 문장으로 한 개의 학생을 삭제

```sql
DELETE FROM 학생 WHERE 이름 = '김소연';
```



**사용자 인터페이스(UI)**

**UI**는 사용자가 제품/서비스를 사용할 때, 마주하게 되는 면. 즉, 사용자가 제품/서비스와 상호작용할 수 있도록 만들어진 매개체

CLI(Command Line Interface) : 텍스트 형태

GUI(Graphical User Interface) : 아이콘이나 메뉴를 선택

NUI(Natural User Interface) : 사용자의 말이나 행동으로 조작



> ##### 자소서 예시   

나는 오라클을 CLI 환경에서 다루기가 편합니다

CLI환경에서 많이 익혔습니다



### DATA BASE Table이란? (6)

DML 문장으로 학과명을 변경

```sql
UPDATE 학생 SET 학과 = '의료기기학' WHERE 학번 = 201443577;
```



## 스키마 다이어그램

데이터베이스 스키마는 주 키와 외래 키 종속성을 가지고 있는데, 이는 **스키마 다이어그램(schema diagram)**을 이용하여 시각적으로 나타낼 수 있다. 

각 릴레이션은 네모 상자로 나타낼 수 있으며, 해당 릴레이션의 속성은 네모 상자 안에 나열되고 릴레이션의 이름은 네모 상자 위에 쓴다. 주 키로 쓰이는 속성은 선을 그어서 표현한다. **외래 키 종속성은 참조하는 릴레이션의 외래 키 속성으로부터 참조된 릴레이션의 주 키로 이르는 화살표로 나타낸다.**

  **참조 무결성 제약조건은 외래 키에 비해서 스키마 다이어그램에 잘 표현되지 않는다.** 



### 💻(실습준비) 사원 Table 생성

```sql
drop table dept;
create table dept(  
  deptno     int,  
  dname      varchar(14),  
  loc        varchar(13),  
  constraint pk_dept primary key (deptno)  
);

drop table emp;
create table emp(  
  empno    int,  
  ename    varchar(10),  
  job      varchar(9),  
  mgr      int,  
  hiredate date,  
  sal      int,  
  comm     int,
  deptno   int,  
  constraint pk_emp primary key (empno),  
  constraint fk_deptno foreign key (deptno) references dept (deptno)
);
```



### 💻(실습준비) 사원 Table 생성 source

```sql
insert into dept (deptno, dname, loc) values (10, 'sales', 'seoul');
insert into dept (deptno, dname, loc) values (20, 'hr', 'deajeon');
insert into dept (deptno, dname, loc) values (30, 'service', 'pusan');
insert into dept (deptno, dname, loc) values (40, 'research', 'jeju');
```



## SELECT와 FROM절

```sql
SELECT country FROM emp;
SELECT DISTINCT job FROM emp;
SELECT empno, ename FROM emp;
SELECT empno, mgr FROM emp ORDER BY empno;
SELECT empno, lename FROM emp ORDER BY 1;
SELECT empno, job + '' + sal FROM emp;
```



> ##### vim

**Vim**(빔, Vi IMproved)은 Bram Moolenaar가 만든 vi 호환 텍스트 편집기이다. CUI용 **Vim**과 GUI용 gVim이 있다. 본래 아미가 컴퓨터 용 프로그램이었으나 현재는 마이크로소프트 윈도우, 리눅스, 맥 오에스 텐을 비롯한 여러 환경을 지원한다.

업무 환경에서는 vim 이 디폴트 설치 → 환경변수 불러서 냅다  뜯어 고쳐야함



## WHERE절과 filtering

### WHERE절과 filtering (1)

```sql
insert into emp values (1001, 'gates', 'chairman', null, '19771117', 5000, null, 10);
insert into emp values (1204, 'sunny', 'manager', 1001, '19890923', 4100, null, 20);
insert into emp values (1321, 'jone', 'manager', 1001, '19990301', 3800, null, 30);
insert into emp values (2034, 'martin', 'member', 1321, '19970513', 2000, null, 30);
```



### WHERE절과 filtering (2)

```sql
select empno, ename, job, mgr, sal, comm, deptno from emp;	
```



### WHERE절과 filtering (3)

```sql
-- 사원명이 'kim'인 시각되는 사람 검색
select empno, ename from emp where ename = 'kim';

-- 사원명이 'j'로 시각되는 사람 검색
select empno, ename from emp where ename like 'j%';

-- 입사일이 1999년 03월 01일인 사람 검색
select empno, hiredate, ename from emp where hiredate = '19990301';

-- 입사일이 1999년 03월 01일 이후인 사람 검색
select empno, hiredate, ename from emp where hiredate < '1999031'

-- 입사일이 1999년 03월 01일 이후 이면서, 부서번호가 20인 사람 검색
select empno, hiredate, ename, deptno from emp where hiredate < '19990301' and deptno = 20;
```



### WHERE절과 filtering (4)

```sql
-- job title이 manager인 사람의 연봉순으로 나열
select empno, ename, job, mgr, sal, comm, deptno from emp where job = 'manager' order by sal;

-- job title이 manager인 사람의 연봉순(내림차순)으로 나열
select empno, ename, job, mgr, sal, comm, deptno from emp where job = 'manager' order by sal desc; 

-- job title이 manager인 사람의 연봉순으로 나열하고, 부서번호로 나열
select empno, ename, job, mgr, sal, comm, deptno from emp where job = 'manager' order by sal, deptno;

-- 입사일을 표현하는데 부서가 서울인 사람을 나열
select empno, loc, hiredate from emp, dept where loc = 'seoul' order by hiredate;
```



## 변수의 사용

### 변수의 사용 (1)

year

```sql
select deptno as 부서명, year(hiredate) as 입사년, ename from emp order by 1, 2;
```

### 변수의 사용 (2)

max

```sql
select ename, max(sal) as 연봉 from emp group by ename;
```

### 변수의 사용 (3)

sum

```sql
select deptno, sum(sal) as 부서연봉총합 from emp where sal > 2000 group by deptno having sum(sal) > 5000;
```



## ORDER BY절

```sql
select top(3) * from emp order by sal;
```



## SQL JOIN

### SQL JOIN(1) Cross Join

```sql
select * from emp cross join dept;
```

Database는 여러개의 Table로 구성되어 있고 하나의 데이터베이스 또는 여러 데이터베이스에 분산되어 있어, 각각의 table을 join하여 사용한다.

여러개의 table로 데이터를 분할하는 작업을 normalized(정규화)한다고 하며, 그 반대의 경우를 De-normalized(비정규화)한다고 명명한다.

정규화는 database에 동일 필드에 중복입력을 예방할 수 있으며, table에 속하여 있는 field의 무결성을 유지시키는데 도움이 된다.

- 단점은 하나의 table에 여러개의 field를 두어 사용할 수 있으나, 과거에는 computing power가 부족하여 resource절약에 초점이 맞추어져서 많이 사용되었다.

관계형 데이터베이스는 많은 부분 JOIN operation이 필요하며, Big data operation에서는 bulk data를 바로 사용하는 경우가 많다.

JOIN operation은 database에 많은 부담을 줄 수 있으며, 사용시 매우 주의가 필요하다.

- 예. 10,000 * 10,000 = 10,000,000,000 (10억)



### SQL JOIN(2) Inner Join

일반적인 inner operation의 형태

```sql
select * from emp inner join dept on emp.deptno = dept.deptno;
```



### 다른 SQL JOIN의 종류

SQL JOIN(3) **Left Outer Join**

SQL JOIN(4) **Right Outer Join**

SQL JOIN(5) **Full Outer Join**

SQL JOIN(6) **Self Join**

SQL JOIN(7) **Anti Join**



## SQL Sub queries

하나의 SQL문 안에 포함된 또 다른 SQL 문

- 2-3 depth가 적당

### SQL Sub queries(1)

Self-Contained Sub queries

```sql
select ename, sal from emp where sal > (select sal 
                                        from emp
                                        where enmae = 'kim');
```



### SQL Sub queries(2)

Self-Contained Sub queries

```sql
# 1
select min(sal) from emp;

# 2
select ename, sal from emp where sal = 2000;
```



### SQL Sub queries(3)

IN 활용 

- 반환되는 값이 멀티값 일때는 IN, 단일값일때는 '='

```sql
select ename, deptno from emp where emp.deptno in (select deptno 
                                                   from dept 
                                                   where loc = 'seoul');
```



## CREATE TABLE

### CREATE TABLE (1)

insert를 위한 Table생성 (oracle 기준)

```sql
create table dept(  
  deptno     int,  
  dname      varchar(14),  
  loc        varchar(13),  
  constraint pk_dept primary key (deptno)  
);
```



### CREATE TABLE (2)

```sql
create table emp(  
  empno    int,  
  ename    varchar(10),  
  job      varchar(9),  
  mgr      int,  
  hiredate date,  
  sal      int,  
  comm     int,
  deptno   int,  
  constraint pk_emp primary key (empno),  
  constraint fk_deptno foreign key (deptno) references dept (deptno)
);
```



### CREATE TABLE (3)

insert를 위한 Table 생성

```sql
insert into dept (deptno, dname, loc) values (10, 'sales', 'seoul');
insert into dept (deptno, dname, loc) values (20, 'hr', 'deajeon');
insert into dept (deptno, dname, loc) values (30, 'service', 'pusan');
insert into dept (deptno, dname, loc) values (40, 'research', 'jeju');

insert into emp values (1001, 'gates', 'chairman', null, '19771117', 5000, null, 10);
insert into emp values (1204, 'sunny', 'manager', 1001, '19890923', 4100, null, 20);
insert into emp values (1321, 'jone', 'manager', 1001, '19990301', 3800, null, 30);
insert into emp values (2034, 'martin', 'member', 1321, '19970513', 2000, null, 30);
insert into emp values (2034, 'herry', 'srmanager', 1001, '19990301', 4500, null, 40);
insert into emp values (2034, 'lee', 'member', 1321, '20010712', 2000, null, 30);
insert into emp values (2034, 'jo', 'member', 1321, '20050719', 2000, null, 30);
insert into emp values (2034, 'jonadan', 'manager', 1001, '20050801', 4000, null, 10);
insert into emp values (2034, 'kim', 'member', 3121, '20050801', 2000, null, 10);
```



## SQL Inserting, Updating and Deleting

### SQL Inserting, Updating and Deleting (1)

INSERT 문장

Table에 여러개의 row를 입력하기 위한 명령

```sql
INSERT INTO <target table> VALUES (col1, col2, ···);
```



### SQL Inserting, Updating and Deleting (2)

INSERT 문장

Table에 여러개의 row를 입력하기 위한 명령

```sql
INSERT INTO dept(deptno, dname, loc) VALUES (50, 'operations', 'sejeong');
```



### SQL Inserting, Updating and Deleting (3)

UPDATE문장

Table에 존재하는row를 수정하기 위한 명령

```sql
UPDATE <target table> SET <col1> = <expression 1>, <col2> = <expression 2>... where <predicate>;
```



### SQL Inserting, Updating and Deleting (4)

UPDATE문장

Table에 존재하는row를 수정하기 위한 명령

```sql
# 변경전
select * from emp where job = 'manager';

# 변경후
UPDATE emp SET job = 'srmanager' where job = 'manager';
```



### SQL Inserting, Updating and Deleting (5)

확인

```sql
select * from emp where job = 'srmanager';
```



### SQL Inserting, Updating and Deleting (6)

DELETE

Table에 하나 또는 그 이상의 row를 삭제하기 위한 명령

```sql
DELETE FROM <table> where <predicate>;	
```



### SQL Inserting, Updating and Deleting (7)

```sql
DELETE FROM emp where mgr = 3328;
```



### SQL Inserting, Updating and Deleting (8)

Truncate

Table 구조는 유지하고 내용을 삭제하기 위한 명령 (DML 처리하지 않아 효과가 좋다.)

```sql
TRUNCATE TABLE emp;
```



## SQL Constraints 실습



## INDEX란?

인덱스란 추가적인 쓰기 작업과 저장 공간을 활용하여 데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조이다. 

만약 우리가 책에서 원하는 내용을 찾는다고 하면, 책의 모든 페이지를 찾아 보는것은 오랜 시간이 걸린다. 그렇기 때문에 책의 저자들은 책의 맨 앞 또는 맨 뒤에 색인을 추가하는데, 데이터베이스의 index는 책의 색인과 같다.

데이터베이스에서도 테이블의 모든 데이터를 검색하면 시간이 오래 걸리기 때문에 데이터와 데이터의 위치를 포함한 자료구조를 생성하여 빠르게 조회할 수 있도록 돕고 있다.

인덱스를 활용하면, 데이터를 조회하는 SELECT 외에도 UPDATE나 DELETE의 성능이 함께 향상된다. 그러한 이유는 해당 연산을 수행하려면 해당 대상을 조회해야만 작업을 할 수 있기 때문이다.

만약 index를 사용하지 않은 컬럼을 조회해야 하는 상황이라면 전체를 탐색하는 Full Scan을 수행해야 한다. Full Scan은 전체를 비교하여 탐색하기 때문에 처리 속도가 떨어진다.



### 인덱스의 관리

 DBMS는 index를 항상 최신의 정렬된 상태로 유지해야 원하는 값을 빠르게 탐색할 수 있다. 그렇기 때문에 인덱스가 적용된 컬럼에 INSERT, UPDATE, DELETE가 수행된다면 각각 다음과 같은 연산을 추가적으로 해주어야 하며 그에 따른 오버헤드가 발생한다. 

- INSERT: 새로운 데이터에 대한 인덱스를 추가함
- DELETE: 삭제하는 데이터의 인덱스를 사용하지 않는다는 작업을 진행함
- UPDATE: 기존의 인덱스를 사용하지 않음 처리하고, 갱신된 데이터에 대해 인덱스를 추가함



### 인덱스의 장점과 단점

**장점**

- 테이블을 조회하는 속도와 그에 따른 성능을 향상시킬 수 있다.
- 전반적인 시스템의 부하를 줄일 수 있다.

**단점**

- 인덱스를 관리하기 위해 DB의 약 10%에 해당하는 저장공간이 필요하다.
- 인덱스를 관리하기 위해 추가 작업이 필요하다.
- 인덱스를 잘못 사용할 경우 오히려 성능이 저하되는 역효과가 발생할 수 있다.

만약 CREATE, DELETE, UPDATE가 빈번한 속성에 인덱스를 걸게 되면 인덱스의 크기가 비대해져서 성능이 오히려 저하되는 역효과가 발생할 수 있다. 그러한 이유 중 하나는 DELETE와 UPDATE 연산 때문이다. 앞에서 설명한대로, UPDATE와 DELETE는 기존의 인덱스를 삭제하지 않고 '사용하지 않음' 처리를 해준다고 하였다. 만약 어떤 테이블에 UPDATE와 DELETE가 빈번하게 발생된다면 실제 데이터는 10만건이지만 인덱스는 100만 건이 넘어가게 되어, SQL문 처리 시 비대해진 인덱스에 의해 오히려 성능이 떨어지게 될 것이다. 



### 인덱스를 추가하면 좋은 경우

- 규모가 작지 않은 테이블
- INSERT, UPDATE, DELETE가 자주 발생하지 않는 컬럼
- JOIN이나 WHERE 또는 ORDER BY에 자주 사용되는 컬럼
- 데이터의 중복도가 낮은 컬럼
- 기타 등등

인덱스를 사용하는 것 만큼이나 생성된 인덱스를 관리해주는 것도 중요하다. 그렇기 때문에 사용하지 않는 인덱스는 바로 제거를 해주어야 한다. 



### 인덱스의 자료구조

인덱스를 구현하기 위해서는 여러 가지 자료구조를 사용할 수 있다. 아래에서는 가장 대표적인 해시 테이블과 B+Tree에 대해서 알아보도록 하겠다.

#### 해시 테이블 (Hash Table)

해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠른 데이터 검색이 필요할 때 유용하다. 해시 테이블은 Key값을 이용해 고유한 index를 생성하여 그 index에 저장된 값을 꺼내오는 구조이다.

해시 테이블 기반의 DB 인덱스는 (데이터=컬럼의 값, 데이터의 위치)를 (Key, Value)로 사용하여 컬럼의 값으로 생성된 해시를 통해 인덱스를 구현하였다. 해시 테이블의 시간복잡도는 O(1)이며 매우 빠른 검색을 지원한다.

하지만 DB 인덱스에서 해시 테이블이 사용되는 경우는 제한적인데, 그러한 이유는 해시가 등호(=) 연산에만 특화되었기 때문이다. 해시 함수는 값이 1이라도 달라지면 완전히 다른 해시 값을 생성하는데, 이러한 특성에 의해 **부등호 연산(>, <)이 자주 사용되는 데이터베이스 검색을 위해서는 해시 테이블이 적합하지 않다.**

즉, 예를 들면 "나는"으로 시작하는 모든 데이터를 검색하기 위한 쿼리문은 인덱스의 혜택을 전혀 받지 못하게 된다. 이러한 이유로 데이터베이스의 인덱스에서는 B+Tree가 일반적으로 사용된다.

###  B+ Tree

B+Tree는 DB의 인덱스를 위해 자식 노드가 2개 이상인 B-Tree를 개선시킨 자료구조이다. B+Tree는 모든 노드에 데이터(Value)를 저장했던 B Tree와 다른 특성을 가지고 있다.

- 리프노드(데이터노드)만 인덱스와 함께 데이터(Value)를 가지고 있고, 나머지 노드(인덱스노드)들은 데이터를 위한 인덱스(Key)만을 갖는다.
- 리프노드들은 LinkedList로 연결되어 있다.
- 데이터 노드 크기는 인덱스 노드의 크기와 같지 않아도 된다.

데이터베이스의 인덱스 컬럼은 부등호를 이용한 순차 검색 연산이 자주 발생될 수 있다. 이러한 이유로 **B Tree의 리프노드들을 LinkedList로 연결하여 순차검색을 용이하게 하는 등 B Tree를 인덱스에 맞게 최적화**하였다. (물론 Best Case에 대해 리프노드까지 가지 않아도 탐색할 수 있는 B Tree에 비해 무조건 리프노드까지 가야한다는 단점도 있다.)

이러한 이유로 비록 B+Tree는 O(log2nlog2n) 의 시간복잡도를 갖지만 해시테이블보다 인덱싱에 더욱 적합한 자료구조가 되었다.

InnoDB에서의 B+Tree는 일반적인 구조보다 더욱 복잡하게 구현이 되었다. InnoDB에서는 같은 레벨의 노드들끼리는 Linked List가 아닌 Double Linked List로 연결되었으며, 자식 노드들은 Single Linked List로 연결되어 있다.



출처: https://mangkyu.tistory.com/96 [MangKyu's Diary]



## MS EXPRESS의 설치

https://www.microsoft.com/ko-kr/download/details.aspx?id=55994



> 미션 크리티컬

리눅스 환경이 되면서 오라클 많이 사용

rdb ms

위키독스에 예제로 배우는 오라클 11g
