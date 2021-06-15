# SQL

SQL(Structured Query Language, 구조화 질의어)은 데이터베이스(DB)에서 필요한 형태의 데이터를 추출 또는 가공하기 위해 사용하는 언어이다.

관계형 데이터베이스 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어



## SQL Syntax

sql은 크게 다음과 같은 형태로 사용된다.

- **SELECT**   칼럼, 계산 값
- **FROM**   테이블 명
- **WHERE**   조건
- **GROUP**
- **BY**   그룹화
- **HAVING**   그룹화에 사용되는 조건



## SELECT

1. 칼럼 조회

   ```sql
   select 호출하려는 칼럼 from DB명.테이블명;
   ```

2. 집계 함수

   ```sql
   select 집계 함수(호출하려는 칼럼) from DB명.테이블명;
   ```

   - 집계 함수 (count(), sum(), avg() 등)

3. *(모든 결과 조회)

   ``` sql
   select * from DB명.테이블명;
   select 칼럼1, 칼럼2 from DB명.테이블명;
   ```

4. AS

   ```sql
   select 칼럼1 as 변경 칼럼 명 from DB명.테이블명;
   ```

5. DISTINCT

   ```sql
   select distinct 칼럼1 from DB명.테이블명;
   ```



## FROM

특정 테이블에 있는 정보를 호출하려면 쿼리에 테이블 명을 지정해 주어야 하는데, 테이블 명은 from절 뒤에 기재한다.

```sql
select 계산식 또는 칼럼 명 from DB명.테이블명;
```

매번 테이블 명에 DB명을 입력하다는 것이 번거롭다면 다음과 같이 처리 가능

```sql
USE DB명;

select 계산식 또는 칼럼 명 from 테이블명;
```

- <u>Error Code: 1046 오류는 DB명을 입력하지 않았을 때 발생</u>
  - 해결방안 
    1. DB명을 입력하여 코드 수정
    2. 해당 스키마를 선택하여 Set as Default Schema



## WHERE

```sql
select 계산식 또는 칼럼 명 from 테이블명 where 조건;
```

1. **BETWEEN**

   ```sql
   select * from DB명.테이블명 where 칼럼 between 시작점 and 끝점;
   ```

2. **대소 관계 표현**

   - | 연산자 | 설명     |
     | ------ | -------- |
     | =      | 동일하다 |
     | >      | 초과     |
     | >=     | 이상     |
     | <      | 미만     |
     | <=     | 이하     |
     | <>     | 같지않다 |

3. **IN**

   ```sql
   select 칼럼 명 from 테이블 명 where 칼럼 명 IN (값1, 값2);
   ```

4. **NOT IN**

   ```sql
   select 칼럼 명 from 테이블 명 where 칼럼 명 NOT IN (값1, 값2)
   ```

5. **IS NULL**

   - NULL: 데이터 수집시 결측치(수집하지 못한 데이터)가 생성되는데, 이러한 결측치를 데이터베이스에서는 NULL로 명칭한다.

     ```sql
     select 칼럼 명 또는 계산식 from 테이블 명 where 칼럼 명 IS NULL;
     ```

   - <u>특정 컬럼값이 NULL이 아닌 것만 출력시</u>

     ```sql
     select 칼럼 명 또는 계산식 from 테이블 명 where 칼럼 명 IS NOT NULL;
     ```

6. **LIKE '%TEXT%'**

   - 특정 필드에 어떤 텍스트가 포함되는 경우를 출력 할 때 사용연산자 LIKE

     ```sql
     select 칼럼 명 from 테이블 명 where 칼럼 명 LIKE '%추출 원하는 특정 텍스트%' ;
     ```

     

     <문제> customer의 address에 ST가 포함된 address_1을 출력 

     ```select address_1 from customer where address like '%ST%'```



**하나만 더**

- 테이블은 칼럼으로 구성되어 있는데 각 컬럼은 데이터 타입을 가진다. 데이터 타입에는 숫자형(Character, Integer), 문자형(Float), 날짜(Data) 등이 있다. 문자형으로 표현하려면 값을 **' '** 로 감싸 주면 된다. 숫자형은 숫자를 그대로 사용하면 된다.



## GROUP BY

칼럼들의 값들을 그룹화해 각 값들의 평균 값, 개수 등을 구할 때 group by이용

group by는 보통 avg, sum, count 등과 같은 집계 함수가 함께 사용

```sql
select 칼럼 명 1, 칼럼 명 2, avg(컬럼 명 3)  from 테이블 명 where 칼럼 명 IN (값1, 값2);
```



**하나만 더**

- 자주 사용하는 3가지 집계 함수는 다음과 같다

| 함수    | 의미        |
| ------- | ----------- |
| AVG()   | 평균        |
| COUNT() | 개수 구하기 |
| SUM()   | 합계        |



**집계 함수에 CASE WHEN 구문 사용하기**

집계 함수 count() 내부에 case when구문을 사용하면 필요한 조건만 집계 할 수 있다.

```sql
select sum(case when 칼럼 = '특정 데이터' then 1 else 0 end) as 별칭 from 테이블
```



<문제> customers테이블을 이용해 USA거주자 수를 계산하고, 그 비중을 구하세요

```sql
select sum(case when country = 'USA' then 1 else 0 end) N-USA, 
       sum(case when country = 'USA' then 1 else 0 end) / count(*) USA_PORTION 
from customers;
```

| N_USA | N_PORTION |
| ----- | --------- |
| 36    | 0.2951    |



## JOIN

데이터는 한 가지 테이블에 적재되지 않는다. 여러 가지 테이블로 분리되어 관리된다. 한 가지 테이블에 모든 정보를 다 담기도 힘들고, 관리 측면에서도 좋은 방법은 아니다.

여러가지 테이블로 나뉜 정보를 조합하려면 테이블 결합 함수를 사용해야 한다. 이 함수를 JOIN이라 한다.ㄴ

1. LEFT JOIN (LEFT OUTER JOIN)

   - left join은 특정 테이블 정보를 기준으로 타 테이블을 결합한다.

   ![SQL LEFT JOIN](https://www.sqltutorial.org/wp-content/uploads/2016/03/SQL-LEFT-JOIN.png)

   ``` sql
   select * 
   from 테이블A 
   left join 테이블B on 테이블A.칼럼1 = 테이블B.칼럼2
   ```

   

2. INNER JOIN

   - inner join은 2가지 테이블에 공통으로 존재하는 정보만 출력된다.

   ![sql-inner-join](https://www.codespot.org/assets/samples/sql-inner-join.png)

   ```sql
   select * 
   from 테이블A 
   inner join 테이블B on 테이블A.칼럼1 = 테이블B.칼럼2
   ```

   

3. FULL JOIN

   - full join은 테이블A 또는 테이블B와 매칭되는 레코드(row값)를 모두 출력한다. 따라서 full join 결과는 매우 큰 데이터 세트가 될 수 있다.

   ![SQL FULL OUTER JOIN](https://www.sqltutorial.org/wp-content/uploads/2016/07/SQL-FULL-OUTER-JOIN.png)

   ```sql
   select * 
   from 테이블A 
   full join 테이블B on 테이블A.칼럼1 = 테이블B.칼럼2
   ```

   



## CASE WHEN

case when 구문은 조건에 따른 값을 다르게 출력하고 싶은 경우 사용된다.

```sql
select case when 조건 1 then 결과 1
when 조건 2 then 결과 2 else 결과3 end
from 테이블 명; 
```



<문제> customers의 country칼럼을 이용해 북미(Canada, USA), 비북미를 출력하는 컬럼을 생성하세요.

```sql
SELECT country, 
       case when country IN ('USA', 'Canada') then 'North America' else 'others' end AS region 
FROM customers
```



|      | country   | region        |
| ---: | --------- | ------------- |
|    1 | France    | others        |
|    2 | USA       | North America |
|    3 | Australia | others        |
|    4 | France    | others        |
|    5 | Norway    | others        |
|    6 | USA       | others        |
|    7 | Poland    | others        |
|    8 | Germany   | others        |
|    9 | USA       | North America |
|   10 | USA       | North America |



<문제> customers의 country칼럼을 이용해 북미(Canada, USA), 비북미를 출력하는 컬럼을 생성하고, 북미, 비북미 거주 고객의 수를 계산하세요.

```sql
SELECT case when country IN ('USA', 'Canada') then 'North America' else 'others' end AS region,
       count(customerNumber) N_CUSTOMERS
FROM customers
GROUP BY case when country IN ('USA', 'Canada') then 'North America' else 'others' end
```



```sql
SELECT case when country IN ('USA', 'Canada') then 'North America' else 'others' end AS region,
       count(customerNumber) N_CUSTOMERS
FROM customers
GROUP BY 1

# group by에서는 칼럼 명을 숫자로 대체 가능하다
# 1은 select에서 첫 번째 칼럼 의미, 2는 select의 두 번째 컬럼 의미
# group by 1은 select의 첫 번째 칼럼으로 그루핑하겠다는 의미다.
```



|      | region        | N_customers |
| ---: | ------------- | ----------- |
|    1 | others        | 83          |
|    2 | North America | 39          |



## RANK, DENSE_RANK, ROW_NUMBER

데이터에 순위를 매기는 데 사용되는 함수에는 **rank, dense_rank, row_number** 3가지 존재

이 3가지 함수의 차이점은 동점일 때의 처리 방법이다. dense_rank, rank는 동점인 경우 같은 등수로 계산한다. 두 함수의 차이는 그다음 등수를 어떤 값으로 매기느냐이다. dense_rank는 동점의 등수 바로 다음 수로 순위를 매기고, rank는 동점인 경우의 데이터 세트를 고려해 다음 등수를 매긴다.

```sql
SELECT row_number() over (order by 칼럼) FROM ···
SELECT rank() over (order by 칼럼) FROM ···
SELECT dense_rank() over (order by 칼럼) from ···
```

order by 의 기본값은 오름차순(asc) 순위 매김. 내림차순으로 순위 매기려면 order by desc

- order by [asc | desc]



## SUBQUERY

IN연산자 이후 ( ) 내의 쿼리를 쿼리 안의 쿼리라는 의미로 subquery라고 한다. 서브쿼리는 굉장히 많이 사용되는 개념인데, in연산자 뿐 아니라 from, join에서도 사용될 수 있다.

```sql
select 칼럼 명 
from 테이블 명 
where 칼럼 명 IN (select 칼럼 from 테이블 where 조건);
```

from, join에 subquery 사용하는 경우

```sql
select 칼럼 명
from (select 칼럼명 from 테이블 명 where 조건) A
```

- from에 서브쿼리를 사용하면 서브쿼리의 실행 결과가 하나의 테이블로 사용된다 from,join에 서브쿼리를 사용하는 경우에는 항상 서브쿼리의 마지막에 'A' 와 같은 문자열을 입력해주어야 한다. 만약 subquery의 마지막에 A라는 문자열을 입력하면, 해당 테이블은 A라는 명칭으로 쿼리 내부에서 사용된다.