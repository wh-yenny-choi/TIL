### SQL 응용

#### DDL

Data Define Language, 데이터 정의어

- `create`, `alter`, `drop`

```mysql
create schema
create domain
create table
create view
create index
alter table
drop
```



**EX**

> patient 테이블에 데이터 타입이 문자 20자리인 'job' 속성 추가

```mysql
alter table patient ADD job CHAR(20);
```

> student 테이블의 ssn속성에 대해, 중복이 허용하지 않도록 'stud_idx'라는 이름으로 오름차순 인덱스를 정의하는 sql문 작성

```mysql
create unique index stud_idx on student(ssn ASC)
```

> 직원 테이블에 대해 '이름' 속성으로 '직원_name' 이라는 인덱스를 정의하는 sql문 작성

```mysql
create index 직원_name on 직원(이름)
```

--------------

#### DCL

Data Contorl Language, 데이터 제어어

- `grant`, `revoke`, `commit`, `rollback`, `savepoint`



**EX**

> 김하늘에게 학생 테이블에 대한 접근 및 조작에 관한 모든 권한을 부여하는 sql문

```mysql
grant all on 학생 to 김하늘
```

> 김하늘에게 강좌 테이블에 대해 삭제하는 권한을 부여하고, 강좌 테이블에 대해 삭제하는 권한을 다른 사람에게 부여할 수 있는 권한을 부여 sql

```mysql
grant delete on 강좌 to 김하늘 with grant option
```

> 임꺽정에서 부여된 교수 테이블에 대한 select, insert, delete 권한을 취소하는 sql문

```mysql
revoke select, insert, delete on 교수 from 임꺽정
```

> 수강 테이블에 대해 임꺽정에게 부여된 update 권한과 임꺽정이 다른 사람에게 update권한을 부여할 수 있는 권한, 그리고 임꺽정이 다른 사람에게 부여한 update 권한도 모두 취소하는 sql문

```mysql
revoke update on 수강 from 임꺽정 CASCADE
```

------------------------------

#### DML

Data Manipulation Language, 데이터 조작어

- `select`, `insert`, `delete`, `update`
  - select 속성 from 테이블 where 조건
  - insert into 테이블 values (데이터1, 데이터2, ···)
  - delete from 테이블 where 조건
  - updata 테이블 set 속성명 = 데이터 where 조건



**EX**

> 학생 테이블에 학번 0823, 성명 '한국산', 학년 3, 과목 '경영학개론', 연락처 '010' 인 학생정보 입력

```mysql
insert into 학생 values(0823, '한국산', 3, '경영학개론', '010')
```

> 학생 테이블에서 이름이 Scott인 튜플 삭제

```mysql
delete from 학생 where 이름 = Scott
```

> 학부생 테이블에서 '담당관' 이름이 '이'로 시작하는 튜플의 '학과번호'를 999로 갱신

```mysql
update 학부생 set 학과번호 = 999 where 담당관 like '이%'
```

> 사원 테이블에 있는 자료 중 '부서' 가 '기획'인 자료를 검색하여 기획부(성명, 경력, 주소, 기본급) 테이블에 삽입하는 sql문 작성

```mysql
insert into 기획부(성명, 경력, 주소, 기본급)
select 성명, 경력, 주소, 기본급 from 사원 where 부서 = '기획'
```

----------------------------------

#### select 

```mysql
SELECT [predicate][테이블명.]속성명 [AS 별칭][, [테이블명.], 속성명, ...]
[, 그룹함수(속성명)[AS별칭]]
[, window함수 OVER (PARTITION BY 속성명1, 속성명2, ... 
                 	ORDER BY 속성명3, 속성명4, ...)]
FROM 테이블명[, 테이블명, ...]
[WHERE 조건]
[GROUP BY 속성명, 속성명, ...]
[HAVING 조건]
[ORDER BY 속성명 [ASC|DESC]]
```

- predicate
  - `all`, `distinct`, `distinctrow`
- 그룹함수
  - count(속성명)
  - sum(속성명)
  - avg(속성명)
  - max(속성명)
  - min(속성명)
  - stddev(속성명)
  - variance(속성명)
  - ROLLUP(속성명) : 하위 레벨 → 상위 레벨
  - CUBE(속성명) : 상위 레벨 → 하위 레벨
- GROUP BY
  - 특정 속성을 기준으로 **그룹화**하여 검색할 때 사용. 일반적으로 **GROUP BY절은 그룹 함수와 함께 사용**
- HAVING
  - GROUP BY와 함께 사용되며, **그룹에 대한 조건 지정**

##### 하위질의(sub query)

> 취미가 나이트댄스인 사원의 이름과 주소 검색

```mysql
select 이름, 주소
from 사원
where 이름 = (select 이름 from 사원 where 취미 = '나이트댄스')
```



**EX**

> 학생 테이블에서 3, 4학년 학생의 학번과 이름을 검색하는 sql문 작성

```mysql
select 학번, 이름 from 학생 where 학년 in(3, 4)
```

> product 테이블에서 'price'의 속성 값이 NULL인 상품의 name을 오름차순으로 정렬하여 검색하는 sql문 작성

```mysql
select name from product where price is NULL order by name(ASC); 
```

> Sale 테이블에서 판매량(psale)이 10~20 사이인 상품의 코드(pid)를 검색하는 sql문 작성

```mysql
select pid from Sale where psale between 10 and 20
```

> <학생정보> 테이블 '학번'과 <신청정보> 테이블의 '학번'이 같고, <신청정보> 테이블의 '신청번호'와 <결제> 테이블의 '신청번호'가 같은 데이터 중 '신청과목'이 'OpenGL'인 데이터의 '학번', '이름', '결제여부'를 검색하는 sql문 작성

```mysql
select 학생정보.학번, 이름, 결제여부 
from 학생정보, 신청정보, 결제
where 학생정보.학번 = 신청정보.학번 and 신청정보.신청번호 = 결제.신청번호 and 신청과목 = 'OpenGL'
```

> 학생 테이블에서 학년이 3학년 이상이고 점수가 80점 이상인 과목을 중복값을 제거하고 검색

```mysql
select distinct 과목 from 학생 where 학년 >= 3 and 점수 >= 80
```

> 회사원 테이블에서 연락번호가 Null이 아닌 사원명을 모두 검색

```mysql
select 사원명 from 회사원 where 연락번호 is not NULL
```

> customer테이블에서 sql문 작성

```sql
-- id, name 검색
select id, name from customer

-- grade를 중복 없이 검색
select distinct grade from customer

-- 모든 데이터를 ID를 기준으로 내림차순 정렬하여 검색
select * from customer order by ID DESC

-- AGE가 입력되지 않은(NULL) NAME을 검색
select NAME from customer where AGE is NULL

-- AGE가 입력된 NAME을 검색
select NAME from customer where AGE is not NULL
```

> 그룹 지정 검색

```sql
-- 상여금 테이블에서 부서 별 상여금의 평균 
select 부서, avg(상여금) AS 평균 from 상여금 group by 부서

-- 상여금 테이블에서 부서별 튜플 수 검색
select 부서, count(*) AS 사원수 from 상여금 group by 부서

-- 상여금 테이블에서 상여금이 100이상인 사원이 2명 이상인 부서의 튜플 수 구하기
select 부서, count(*) AS 사원수 from 상여금 where 상여금 >= 100 group by 부서 having count(*) >= 2

-- 상여금 테이블의 부서, 상여내역, 상여금에 대해 부서별 상여내역별 소계와 전체 합계 검색
select 부서, 상여내역, sum(상여금) AS 상여금 합계 from 상여금 group by rollup(부서, 상여내역)
```

> <학생정보> 테이블의 학번과 <신청정보> 테이블의 학번이 같고, 신청과목이 'Java'인 학생들만을 대상으로 '이름', '전공', '신청과목'을 검색하려 한다. 
>
> 검색된 데이터는 '이름', '전공', '신청과목'을 기준으로 그룹을 지정하되 '전공'이 '컴퓨터공학' 인 그룹만 표시

```sql
select 이름, 전공, 신청과목
from 학생정보, 신청정보
where 학생정보.학번 = 신청정보.학번 and 신청과목 = 'Java' group by 이름, 전공, 신청과목 having 전공 = '컴퓨터공학'
```

> <결제> 테이블을 이용하여 결제여부별 학생수 검색

```sql
select 결제여부, count(*) AS 학생수
from 결제
group by 결제여부
```

> 테이블 지점정보(지점코드, 소속도시, 매출액)
>
> 지점이 세 군데 이상 있는 도시에 대해 각 도시별로 그 도시에서 매출액이 1000을 초과하는 지점들의 평균 매출액 구하기

```sql
select 소속도시, avg(매출액)
from 지점정보 
where 매출액 > 1000
group by 소속도시
having count(*) >= 3
```

--------------

**문제**

1. 직원 테이블을 삭제하는 sql문 작성

```sql
drop table 직원
```

3. 사원 테이블의 모든 데이터를 검색하는 sql 작성

```sql
select * from 사원
```

4. 자격증 취득 경력이 3년 이상인 사원의 '이름'을 검색하되, 같은 이름은 한 번만 나오게 sql문 작성

```mysql
select distinct 이름 from 자격증 where 경력 >= 3
```

5. 하위 질의를 이용하여 사원 중에 자격증이 없는 사원의 이름,  재직년도, 기본급을 검색하는 sql문 작성

```sql
select 이름, 재직년도, 기본급 from 사원 where 이름 not in (select 이름 from 자격증)
```

6. 자격증을 2개 이상 가진 사원의 '이름'을 검색하는 sql문 작성

```sql
select 이름 from 자격증 group by 이름 having count(*) >= 2
```

7. <학생> 테이블에서 3학년 학생에 대한 모든 속성을 추출한 <3학년 학생> 뷰를 정의하는 sql문 자성

```sql
create view 3학년 학생 AS select * 
from 학생 where 학년 = 3 with check option

-- create view 뷰명[(속성명[, 속성명])] AS SELECT 문
```

8. 강좌 테이블과 교수 테이블에서 '교수번호'가 같은 튜플을 조인하여 강좌명, 강의실, 수강제한인원, 교수이름 속성을 갖는 <강좌교수> 뷰를 정의하는 sql문 작성

```sql
create view 강좌교수(강좌명, 강의실, 수강제한인원, 교수이름) as select 강좌명, 강의실, 수강제한인원, 교수이름
from 강좌, 교수 where 강좌.교수번호 = 교수.교수번호
```

10. 홍길동에서 강좌 테이블을 검색하는 권한을 부여하는 sql문 작성

```sql
grant select on 강좌 to 홍길동
```

11. 홍길동에게 학생 테이블에 대한 접근 및 조작에 관한 모든 권한을 부여하고, 해당 권한을 다른 사람에게 부여할 수 있는 권한을 부여하는 sql 문 작성

```sql
grant all on 학생 to 홍길동 with grant option
```

12. 박문수에게 부여된 교수 테이블에 대한 insert 권한을 취소하는 sql문 작성

```sql
revoke insert on교수 from 박문수
```

13. 수강 테이블에 대해 박문수에게 부여된 select권한과 박문수가 다른 사람에게 select 권한을 부여할 수 있는 권한 그리고 박문수가 다른 사람에게 부여한 select 권한을 모두 취소하는 sql문 작성

```sql
revoke select on수강 from 박문수 cascade
```

14. <상품> 테이블에서 제품코드가 P-20로 중복인 상품을 모두 삭제한 후 ('P-20', 'player', '8800', '6600') 인 제품을 다시 입력하는 sql문 작성

```sql
delete from 상품 where 제품코드 = 'P-20'
insert into 상품 values('P-20', 'player', '8800', '6600')
```

15. 총액이 가장 큰 거래처의 상호와 총액을 검색하는 sql문 작성

```sql
select 상호, 총액 from 거래내역 where 총액 in(select max(총액) from 거래내역)
```

16. 사원, 연락처 테이블에서 성별이 여자고, 사번이 같은 성명, 나이, 직책 검색

```sql
select 성명, 나이, 직책 from 사원, 연락처 where 연락처.성별 = '여' and 사원.사번 = 연락처.사번
```

17. 학번이 S로 시작하는 3글자 표시

```sql
select 학번, 이름 from 성적 where 학번 like 'S _ _'

-- % : 모든 문자 대표
-- _ : 문자 하나 대표
-- # : 숫자 하나 대표
```

21. 지원ID, 이름, 지원학과, 연락처 속성 표시, <지원자> 테이블 대상, 점수가 60점 이상인 지원자만 검색, 지원학과를 기준으로 오름차순 정렬하고, 지원학과가 같은 경우 점수를 기준으로 내림차순 정렬

```sql
select 지원ID, 이름, 지원학과, 연락처
from 지원자
where 점수 > 59 
order by 지원학과, 점수 DESC
```

22. 학생 테이블에 주소 필드를 추가하는 sql문 작성

```sql
alter table 학생 add 주소
```

23. 공급자 테이블에 대해 공급자명에 신이 들어가 있는 모든 필드를 검색하는 sql문 작성

```sql
select * from 공급자 where 공급자명 like '%신%''
```

24. 책명이 운영체제인 책번호를 검색하는 sql문 작성

```sql
select 가격 from 도서가격
where 책번호 = (select 책번호 from 도서 where 책명 = '운영체제')
```

25. 성적 테이블에 이름이 'LEE' 인 모든 튜플의 '점수' 속성에 10을 더한다

```sql
update 성적 set 점수 = 점수 + 10 where 이름 = 'LEE' 
```

27. 빈칸 채우기

```sql
insert into 합격명부 select FUNC_GEN(등록번호, 학과), 이름, 학과, 전화번호 from 입시명부
```

-----------------

### JOIN

**종류**

- Natrual Join

- Inner Join
- Outer Join
  - Left Join
  - Right Join
- Cross Join



![img](https://blog.kakaocdn.net/dn/b8YNAm/btrbCuoZPrI/lEIcImHWTIZs3nApw0Bqr0/img.png)



#### Inner Join

- 교집합
- 기준 테이블과 Join한 테이블의 **중복된 값** 보여줌
- 결과값은 A의 테이블과 B테이블이 모두 가지고 있는 데이터만 검색

```sql
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
INNER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키...

--예제--
SELECT
A.NAME,  # A테이블의 NAME조회
B.AGE  #B테이블의 AGE조회
FROM EX_TABLE A
INNER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```



#### left outer join

<img src="https://t1.daumcdn.net/cfile/tistory/997E7F415A81490507" alt="JOIN2" style="zoom:50%;" />

- **기준 테이블의 값 + 테이블과 기준 테이블의 중복된 값**

- 왼쪽 테이블(A)을 기준으로 join
  - 결과값 : A테이블의 모든 데이터와 A와 B의 중복값 검색

```sql
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
LEFT OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키...

--예제--
SELECT
A.NAME,  # 테이블의 NAME조회
B.AGE  # B테이블의 AGE조회
FROM EX_TABLE A
LEFT OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```



#### right outer join

<img src="https://t1.daumcdn.net/cfile/tistory/9984CE355A8149180A" alt="JOIN3" style="zoom:50%;" />

- **기준 테이블의 값 + 테이블과 기준 테이블의 중복된 값**

- 오른쪽 테이블(B)을 기준으로 join
  - 결과값 : B테이블의 모든 데이터와 A와 B의 중복값 검색

```sql
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
RIGHT OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키...

--예제--
SELECT
A.NAME,  # A테이블의 NAME조회
B.AGE  # B테이블의 AGE조회
FROM EX_TABLE B
RIGHT OUTER JOIN JOIN_TABLE A ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```



#### full outer join

<img src="https://t1.daumcdn.net/cfile/tistory/99195F345A8149391B" alt="JOIN4" style="zoom:50%;" />

- 합집합
- A테이블, B테이블이 가지고 있는 **데이터가 모두 검색**
- 사실상 기준 테이블의 의미❌

```sql
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
FULL OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키...

--예제--
SELECT
A.NAME,  # A테이블의 NAME조회
B.AGE  # B테이블의 AGE조회
FROM EX_TABLE A
FULL OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```

--------------------

### Union

- union은 여러개의 sql문을 합쳐 하나의 sql 문으로 만들어주는 방법
- 두 개의 쿼리의 합집합을 만들어 준다

#### Union과 UnionAll의 차이점

- Union : 두 쿼리의 결과의 중복값을 제거
- UnionAll : 중복된 값도 전부 다 보여준다
- 속도 비교 : (빠름) UnionAll > Union

#### Union 사용시 주의점

- 칼럼명이 같아야 함
  - 같지 않은 경우 `as`를 사용하여 같게 만들어 주면 된다
- 칼럼 별 데이터 타입이 같아야 한다

```sql
-- 두 개의 테이블 죄회 쿼리문 합집합 구하기
SELECT * FROM EX_TABLE1
Union/UnionAll
SELECT * FROM EX_TABLE2

-- 품목별 총합계금액 구하기
SELECT
COMPANY, 
ITEM,
MAX(AM) AS AM,
MAX(QT_IO) AS QT_IO,
MAX(AM_RETURN) AS AM_RETURN,
MAX(QT_RETURN) AS QT_RETURN,
MAX(AM)*MAX(QT_IO)-MAX(AM_RETURN)*MAX(QT_RETURN) AS AM_TOT
FROM
(
    SELECT
    COMPANY,
    ITEM,
    AM,
    QT_IO,
    '0'AM_RETURN,
    '0'QT_RETURN
    FROM EX_TABLE01
UNION ALL
    SELECT
    COMPANY,
    ITEM,
    '0'AM,
    '0'QT_IO,
    AM AS AM_RETURN,
    QT_RETURN
    FROM EX_TABLE02
)UN
group by COMPANY,ITEM
```

-----------

#### 문제 풀이 +

```sql
SET @변수명 = '값';
SET @변수명 := '값'; 
위의 2가지 방법으로 MySQL에서 변수를 선언할 수 있습니다.

SET 명령어를 사용한 변수 선언 시 '=' 와 ':=' 2가지 방법은 차이가 없습니다.
하지만 SET을 제외한 다른 쿼리문(SELECT 등)은 '=' 를 비교연산자(comparison operator)로 인식하기 때문에, SET이 아닌 쿼리문에서는 반드시 대입 연산자(assignment operator) ':='을 사용해 야 합니다.
결론적으로 보면 '='와 ':=' 차이는 아래와 같습니다.
'=' : MySQL에서 대입연산자, 비교연산자 2가지로 사용 됨 (SET 명령어에서만 대입 연산자로 인식)
':=' : MySQL에서 대입 연산자로만 사용 됨 
변수 사용 시 명시적으로 대입 연산자의 의미만을 갖는 ':=' 의 사용을 권장합니다. 



IFNULL(A, B)
A가 NULL이면 B를, 그렇지 않다면 A를 반환


IF(조건문, TRUE, FALSE)


2015라면 %y = 15, %Y = 2015


datetime type은 뺄셈이 가능
```

