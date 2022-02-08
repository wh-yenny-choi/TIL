# 5장

> ## 스파크 SQL로 멋진 쿼리를 실행하자

**학습 내용**

- DataFrame을 생성하는 방법
- DataFrame API 사용법
- Dataset 소개
- SQL 쿼리 사용법
- 외부 데이터를 로드 및 저장하는 방법
- 카탈리스트 최적화 엔진
- 텅스텐 프로젝트의 스파크 성능 향상



## 5.1 DataFrame다루기



![img](https://thebook.io/img/006908/spark171.jpg)

- 두 클라이언트가 스파크 SQL을 사용해 동일한 쿼리를 실행하는 예(첫 번째 클라이언트는 DataFrame DSL을 사용하는 스파크 애플리케이션이고, 두 번째 클라이언트는 JDBC를 사용하는 비-스파크 클라이언트 애플리케이션이다. 두 클라이언트 모두 관계형 데이터베이스에 저장된 테이블과 HDFS에 저장된 Parquet 파일 데이터를 조인하는 쿼리를 동일하게 실행한다.)

 

### 5.1.1 RDD에서 DataFrame 생성

> **스파크 DataFrame은 SQL 및 도메인 특화 언어(DSL)로 작성된 표현식을 최적화된 하위 레벨 RDD연산으로 변환한다.**

DataFrame을 생성할 때는 데이터를 먼저 RDD로 로드한 후 DataFrame으로 변환하는 방법을 가장 많이 사용 

- 정형화 과정으로,
- 즉, 비정형 데이터에 DataFrame API을 사용하려면
  - 먼저 이 데이터를 RDD로 로드하고 
  - 변환한 후 
  - 이 RDD에서 DataFrame을 생성해야 함

**예시**

로그 파일을 DataFrame으로 가져오려면,

- 먼저 파일을 RDD로 로드
- 각 줄을 파싱
- 로그의 각 항목을 구성하는 하위 요소 파악



RDD 에서 DataFrame 생성 방법

1. 로우 데이터를 튜플 형태로 저장한 RDD 사용 방법
2.  케이스 클래스를 사용하는 방법
3. 스키마를 명시적으로 지정하는 방법



**로우 데이터를 튜플 형태로 저장한 RDD 사용 방법**

- 장점 : 가장 기초적, 간단
- 단점 : 스키마 속정을 전혀 지정할 수 없음 ⇒ <u>제한적</u>

**케이스 클래스를 사용하는 방법**

- 장점 : 1번 방법만큼 제한적이지 <u>않음</u>
- 단점 : 케이스 클래스를 작성하는 것으로 조금 더 복잡

**스키마를 명시적으로 지정하는 방법**

- 스파크 표준 처럼 널리 사용됨
- 3번은 스키마를 명시적으로 지정
  - 1, 2번 방법은 스키마를 간접적으로 지정(추론)



#### 5.1.1.1 SparkSession을 생성하고 암시적 메서드 임포트

```
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder().getOrCreate()

# RDD에서 DataFrame 생성 
# 스파크 쉘 실행시 자동 시작 됨
import spark.implicits._
```



#### 5.1.1.2 예제 데이터셋 로드 및 파악

```
## 예제 로드

# 데이터 파싱, RDD로 로드
val itPostsRows = sc.textFile("first-edition/ch05/italianPosts.csv")

# 문자열 배열로 구성된 RDD 반환
# 배열의 각 문자열을 각기 다른 칼럼으로 매핑
# RDD의 toDF메서드 호출 → 문자열 배열 타입의 다닐 칼럼을 가진 DataFrame
val itPostsSplit = itPostsRows.map(x => x.split("~"))
```



#### 5.1.1.3 튜플 형식의 RDD에서 DataFrame 생성 

> RDD 에서 DataFrame 생성 방법
>
> 1. 로우 데이터를 튜플 형태로 저장한 RDD 사용 방법

```
## 튜플 형식의 RDD에서 DataFrame 생성

# 예제 RDD의 배열을 튜플로 변환하고 toDF를 호출해서 DataFrame 생성
# **배열을 튜플로 변환하는 깔끔한 방법은 없다.** (다음과 같이 번거로운 표현식으로 해결)
val itPostsRDD = itPostsSplit.map(x => (x(0),x(1),x(2),x(3),x(4),x(5),x(6),x(7),x(8),x(9),x(10),x(11),x(12)))

# 반환된 RDD의 toDF함수 호출, DataFrame 생성
val itPostsDFrame = itPostsRDD.toDF()

# DataFrame API제공하는 기능 사용 가능
# show 메서드를 인수 없이 호출시, 기본으로 상위 20개 로우 출력
# show 메서드를 호출, 상위 열 개 로우 내용을 정돈된 형식으로 출력
itPostsDFrame.show(10)

# toDF 메서드에 칼럼 이름 전달 
val itPostsDF = itPostsRDD.toDF("commentCount", "lastActivityDate", "ownerUserId", "body", "score", "creationDate", "viewCount", "title", "tags", "answerCount", "acceptedAnswerId", "postTypeId", "id")

# printSchema 메서드는 DataFrame이 가진 칼럼 정보 출력
# printScheme 메서드로 DataFrame 스키마 확인
itPostsDF.printSchema
```

- RDD를 DataFrame으로 변환할 때 칼럼 이름과 데이터 타입을 지정할 수 있는 방법? 



#### 5.1.1.4 케이스 클래스를 사용해 RDD를 DataFrame으로 변환

RDD를 DataFrame으로 변환하는 두 번째 방법

- RDD의 각 로우를 케이스(case)클래스로 매핑한 후 toDF 메서드  호출

> RDD 에서 DataFrame 생성 방법
>
> 1. 로우 데이터를 튜플 형태로 저장한 RDD 사용 방법
> 2.  케이스 클래스를 사용하는 방법

변환에 앞서 먼저 RDD 데이터를 저장할 케이스 클래스 정의

```
# 예제 데이터셋의 각 로우를 저장할 Post 클래스 선언
import java.sql.Timestamp
case class Post (commentCount:Option[Int], lastActivityDate:Option[java.sql.Timestamp],
  ownerUserId:Option[Long], body:String, score:Option[Int], creationDate:Option[java.sql.Timestamp],
  viewCount:Option[Int], title:String, tags:String, answerCount:Option[Int],
  acceptedAnswerId:Option[Long], postTypeId:Option[Long], id:Long)

```



181~196



## 5.2 DataFrame을 넘어 Dataset으로



## 5.3 SQL 명령 🌟

> DataFrame을 참조해 
>
> - SQL 쿼리를 작성하고 실행하는 방법 
> - 쓰리프트 서버로 스파크 클러스터에 연결하는 방법

SQL 명령 

- 스파크 SQL 프로그램을 작성할 수 있는 또 다른 인터페이스

- DataFrame DSL 기능을 SQL 명령에서도 동일하게 사용할 수 있다.
- DSL보다 SQL 작성이 용이한 사용자
  - 분산 데이터베이스 작업(관계형 데이터베이스, 하이브 등)에 익숙한 사용자

스파크 SQL

- 사용자가 작성한 sql 명령을 DataFrame 연산으로 변환
- 스파크의 sql 명령은 오직 sql인터페이스에만 익숙한 사용자에게 스파크 sql과 DataFrame을 활용하는 기회 제공
  - sql사용자는 스파크의 쓰리포트 서버로 연결된 표준 JDBC 또는 ODBC 프로토콜로 자신이 사용하던 일반 SQL 애플리케이션에서도 스파크에 접속할 수 있다



> DBMS 접속 기술

특정 application에서 DB접근 시 접근 기술 필요

JDBC ( Java Database Connectivity) : 자바 인터페이스

-  Java 언어로 다양한 종류의 DB에 접속, SQL문을 수행할 때 사용하는 표준 API

- 접속하려는 DBMS에 대한 드라이버 필요

- Java SE(Standard Edition)에 포함, JDBC 클래스는 java, sql, javax.sql에 포함

  

ODBC(Open Database Connectivity) : 커넥션 해주는 인터페이스

- DB에 접근하기 위한 표준 개방형 API, 개발 언어에 관계 없이 사용 가능

- 프로그램 내 ODBC 문장을 사용하여 MS-Access, DBase, DB2, Excel, Text 등 다양한 DB에 접근 가능

- 접속하려는 DBMS에 대한 드라이버가 필요하지만, 해당 DBMS의 인터페이스를 모르더라도 ODBC 문장을 사용하여 SQL을 작성하면 ODBC에 포함된 드라이버 관리자가 자동으로 연결한다.

- DBMS의 인터페이스에 맞게 연결해주므로 DBMS의 종류를 몰라도 됨



스파크 지원 SQL언어 

- 스파크 전용 SQL
- 하이브 쿼리 언어(HQL)
  - 더 풍부한 기능 제공
  - 하이브 기능 사용하려면 하이브를 지원하는 스파크 배포판 필요 
    - ⇒ 스파크 아카이브



### 5.3.1 테이블 카탈로그와 하이브 메타스토어

사용자가 작성한 SQL명령을 DataFrame 연산으로 변환

Spark 전용 SQL, Hive의 HQL 지원

테이블 카탈로그와 하이브 메타스토어

- 테이블 카탈로그 : 사용자가 등록한 테이블 정보 저장
- 하이브 메타 스토어 : 영구적 DB. Spark Session을 종료하여도 정보 유지



#### 5.3.1.1 테이블을 임시로 등록

스파크 (하이브 지원)에서 임시로 테이블 정의 저장 가능

`createOrReplaceTempView` 메서드 사용 하여 DataFrame을 임시 테이블로 등록

- 하이브 지원 스파크와 미지원 스파크에서 동일하게 사용 

- 예시 

  ```
  # postsDf DataFrame을 임시로 등록
  postsDf.createOrReplaceTempView("posts_temp")
  ```

  sql쿼리에서` posts_temp `이름을 참조해 `postsDf DataFrame` 데이터에 질의 실행 가능

#### 5.3.1.2 테이블을 영구적으로 등록

#### 5.3.1.3

#### 5.3.1.4



### 5.3.2 SQL 쿼리 실행 🌟🌟🌟

**스파크 SQL은 DataFrame DSL이 지원하는 모든 데이터 작업을 똑같이 지원할 수 있을 뿐 아니라, 더 많은 기능을 제공한다.**

```
# spark-shell 종료 후 진행
spark@spark-in-action:~$ spark-sql

# posts테이블에서 가장 최근에 게시된 질문 세 개의 제목 출력
# spark sql 셸에서는 sql표현식 마지막에 세미콜론 (;) 붙여야함
select substring(title, 0, 70) from posts where postTypeId = 1 order by creationDate desc limit 3;
```





## 5.4 DataFrame을 저장하고 불러오기🌟

스파크는 다양한 기본 파일 포맷 및 데이터베이스 지원

JDBC, Hive, JSON, ORC, Parquet 등



### 5.4.1 기본 데이터 소스 🌟

#### 5.4.1.1 JSON 

XML을 대체하는 경량(light weight) 데이터 포맷



#### 5.4.1.2 ORC (Optimizer Row Columnar)

RCFile포맷보다 효율적으로 Hive Format으로 저장 

- 최근 현장에서 많이 사용



#### 5.4.1.3 Parquet

구조에 중점을 두어 설계

ORC 파일보다 중첩 구조의 데이터 셋을 더 효율적으로 사용 가능



5.4.2.3

5.4.2.4

5.4.2.6





## 5.5 카탈리스트 최적화 엔진

## 5.6 텅스텐 프로젝트의 스파크 성능 향상

## 5.7 요약