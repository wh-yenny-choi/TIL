# JOIN

## 개념

DML - JOIN

- 2개의 테이블에 대해 연관된 튜플들을 결합하여, 하나의 새로운 릴레이션을 반환
- 크게 inner join, outer join으로 구분
- join절은 일반적으로 from절에 기술하지만, 릴레이션이 사용되는 어느 곳에서나 사용할 수 있다.

### 테이블 예시

**<학생>**

| <u>학번</u> | 이름 | 학과코드 | 선배 | 성적 |
| ----------- | ---- | -------- | ---- | ---- |
| 15          | 김   | a        |      | a    |
| 16          | 이   | b        |      | b    |
| 17          | 박   | a        | 15   | c    |
| 18          | 최   | b        | 16   | d    |
| 19          | 강   |          | 17   | f    |



**<학과>**

| <u>학과코드</u> | 학과명 |
| --------------- | ------ |
| a               | 컴공   |
| b               | 통계   |
| c               | 교육   |



## INNER JOIN

- 가장 일반적인 join의 형태
- 관계가 설정된 두 테이블에서 조인된 필드가 일치하는 행만을 표시한다
- where절, natural join, join~using 절을 이용한 표기 형식이 있다

### WHERE 절을 이용한 표기 형식

```sql
select [table1]col,[table2]col from table1, table2 where table1.col = table2.col;	

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학번코드, 학과명 출력
select 학번, 이름, 학생.학과코드, 학과명 
from 학생, 학과
where 학생.학과코드 = 학과.학과코드;
```

### NATURAL JOIN을 이용한 표기 형식

```sql
select [table1]col,[table2]col from table1 natural join table2;

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학번코드, 학과명 출력
select 학번, 이름, 학생.학과코드, 학과명
from 학생
natural join 학과;
```

### JOIN~USING 절을 이용한 표기 형식

```sql
select [table1]col,[table2]col from table1 join table2 using (col); 

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학번코드, 학과명 출력
select 학번, 이름, 학생.학과코드, 학과명 
from 학생
join 학과 using (학과코드);
```



## OUTER JOIN

- 릴레이션에서 join조건에 만족하지 않은 튜플도 결과로 출력하기 위한 join 방법
- left outer join, right outer join, full outer join 이 있다

### LEFT OUTER JOIN

- inner join의 결과를 구한 후, 
- **우측 항** 릴레이션의 어떤 튜플과도 맞지 않는 **좌측 항**의 릴레이션에 있는 튜플들에 
- NULL 값을 붙여서 inner join의 결과에 추가

```sql
select [table1]col, [table2]col from table1 left outer join table2 on table1.col = table2.col;

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학과코드, 학과명 출력. 단, 학과코드가 입력되지 않은 학생도 출력.
select 학번, 이름, 학생.학과코드, 학과명
from 학생 
left outer join 학과 on 학생.학과코드 = 학과.학과코드;
```

**<left outer join  결과>**

| 학번 | 이름 | 학과코드 | 학과명 |
| ---- | ---- | -------- | ------ |
| 15   | 김   | a        | 컴공   |
| 16   | 이   | b        | 통계   |
| 17   | 박   | a        | 컴공   |
| 18   | 최   | b        | 통계   |
| 19   | 강   |          |        |

### RIGHT OUTER JOIN

- inner join의 결과를 구한 후,
- **좌측 항** 릴레이션의 어떤 튜플과도 맞지 않는 **우측 항**의 릴레이션에 있는 튜플들에
- NULL 값을 붙여서 inner join의 결과에 추가

```sql
select [table1]col, [table2]col from table1 right outer join table2 on table1.col = table2.col;

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학번코드, 학과명 출력. 단, 학과코드가 입력되지 않은 학생도 출력.
select 학번, 이름, 학생.학과코드, 학과명 
from 학생 
right outer join 학과 on 학생.학과코드 = 학과.학과코드;
```

**<right outer join 결과>**

| 학번   | 이름   | 학과코드 | 학과명 |
| ------ | ------ | -------- | ------ |
| 15, 17 | 김, 박 | a        | 컴공   |
| 16, 19 | 이, 최 | b        | 통계   |
|        |        | c        | 교육   |

### FULL OUTER JOIN

- inner join의 결과를 구한 후,
- 어느 한쪽 테이블에 값이 있을 경우 튜플들에
- NULL 값을 붙여서 inner join의 결과에 추가

```sql
select [table1]col, [table2]col from table1 left outer join table2 on table1.col = table2.col;

# <학생>, <학과> 테이블 학과코드 값이 같은 튜플을 JOIN하여 학번, 이름, 학과코드, 학과명 출력. 단, 학과코드가 입력되지 않은 학생도 출력.
select 학번, 이름, 학생.학과코드, 학과명 
from 학생 
full outer join 학과 on 학생.학과코드 = 학과.학과코드;
```

**<full outer join 결과>**

| 학번 | 이름 | 학과코드 | 학과명 |
| ---- | ---- | -------- | ------ |
| 15   | 김   | a        | 컴공   |
| 16   | 이   | b        | 통계   |
| 17   | 박   | a        | 컴공   |
| 18   | 최   | b        | 통계   |
| 19   | 강   |          |        |
|      |      | c        | 교육   |

### 

## JOIN 정리

- inner join : 두 테이블 간 조건이 맞는 값만 가져온다
- left outer join : 조건에 맞지 않아도 left에 값이 존재하면 값을 가져온다
- right outer join : 조건에 맞지 않아도 right에 값이 존재하면 값을 가져온다
- full outer join : 두 테이블 중 한 테이블에만 값이 있다면 조건에 맞지 않아도 값을 가져온다.