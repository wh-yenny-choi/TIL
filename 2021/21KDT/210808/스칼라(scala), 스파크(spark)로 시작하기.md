# 스칼라, 스파크로 시작하기

> https://wikidocs.net/book/2350

# 스파크

- 스파크
- 스파크 구조
- 스파크 모니터링 

## 1. 스파크

스파크는 **인메모리 기반의 대용량 데이터 고속처리 엔진**으로 **범용 분산 클러스터 컴퓨팅 프레임워크**

### 스파크의 특징

- speed : 인메모리 기반의 빠른 처리
- ease of use : 다양한 언어 지원을 통한 사용의 편이성 (Java, scala, python, r, sql)
- generality : sql, streaming, 머신러닝, 그래프 연산 등 다양한 컴포넌트 제공
- run everywhere 
  - YARN, Mesos, Kubernetes 등 다양한 클러스터에서 동작 가능
  - HDFD, Casandra, HBase 등 다양한 포맷 지원



#### 인메모리 기반의 빠른 처리

스파크는

- 인메모리(in-memory) 기반 처리
- 맵리듀스 작업처리에 비해 
  - 디스크는 10배
  - 메모리 작업은 100배 빠른 속도
- 맵리듀스는 작업 속도에 제약이 있다
  - IO로 인한 작업 속도에 제약 발생
  - 작업의 중간 결과를 디스크
- 스파크는 반복 작업의 효율이 높다
  - 작업의 중간 결과를 메모리에 저장 

![spark inmemory](https://spark.apache.org/images/logistic-regression.png)



##### 맵리듀스 (MapReduce) 란?

맵리듀스란 **대용량 데이터 처리**를 **분산 병렬 컴퓨팅에서 처리**하기 위한 목적으로 제작한 **소프트웨어 프레임워크**

- 예) 한 명이 4주에 작업할 일을 4명이 나누어 1주일에 끝내는 것
  - 이 개념은 하둡에서 사용하는 병렬 처리 개념
  - 4명의 작업자 = 클러스터(cluster)

- 맵리듀스는 작업의 중간 결과를 디스크에 쓴다 
  - IO로 인한 작업 속도에 제약 발생

**맵(Map)** + **리듀스(Reduce)** 로 이루어져 있다.

- 맵 구조
  - 빅데이터에서 프로세스는 최대한 단순해야 함
    - RDBMS처럼 처리의 순서 필요하거나 데이터 처리 실패로 인해 다시 되돌아가는 복잡한 연산은 어렵다
    - 프로세스를 간단히 하기 위해서는 기준이 되는 값을 하나로 잡아야 한다.
  - 맵에서는 key value를 이용
    - key 값을 이용하면 정렬과 그룹화가 간편해진다.

- 맵리듀스 job들은 jobtracker에 의해 제어된다
  - 잡트래커는 마스터 노드에 존재
  - 이 잡트래커가 클러스터의 다른 노드들에 맵과 리듀스 task를 할당

- 과정 
  - input → splitting → mapping  → shuffling  → reducing → final result
    - input : 데이터 입력 과정
    - splitting : 데이터를 쪼개어(splitting) HDFS에 저장하는 과정
    - mapping : 하나의 값을 다른 값으로 대응
    - shuffling : 맵 함수의 결과를 취합하기 위해 리듀스 함수로 데이터를 전달하는 과정. map task와 reduce task의 중간 단계
    - reducing : 모든 값을 합쳐 원하는 값을 추출
    - final result : 추출된 값을 합침

![img](https://t1.daumcdn.net/cfile/tistory/99F6AA445B5975A320)

![img](https://t1.daumcdn.net/cfile/tistory/99FC4B345B62DEB71C)



### 다양한 컴포넌트 제공

스파크는 단일 시스템 내에서 지원

- 스파크 스트리밍을 이용한 스트림 처리
- 스파크 SQL을 이용한 SQL 처리
- MLib를 이용한 머신러닝 처리
- GraphX를 이용한 그래프 프로세싱

추가적인 소프트웨어 설치 없이도

- 다양한 애플리케이션 구현

각 컴포넌트간의 연계를 이용해

- 애플리케이션 생성도 쉽게 구현



### 다양한 클러스터 매니저 지원

**클러스터 매니저**로

- YERN
- Mesos
- Kubernetes
- standalone 

등 다양한 포맷 지원하여 **운영 시스템 선택에 다양성을 제공**

또한, 

- HDFS
- 카산드라
- HBase
- S3 

등의 **다양한 데이터 포맷을 지원**하여 **여러 시스템에 적용 가능**



### 다양한 파일 포맷 지원 및 Hbase, Hive 등과 연동 가능

스파크는 기본적으로 

- txt
- JSON
- ORC
- Parquet

등의 **파일 포맷 지원**

S3, HDFS등의 **파일 시스템과 연동도 가능**하고,

HBase, Hive와도 간단하게 연동 가능하다



#### HDFS 란?

HDFS는 Hadoop클러스터로 이루어진 File System 

![img](https://t1.daumcdn.net/cfile/tistory/261EE95058D3A77A15)

- HDFS마스터가 담당하는 책임
  - 슬레이브 노드 사이의 저장 공간을 분할하고
  - 데이터 저장 위치를 관리
- 네임노드는 
  - 어떤 데이터노드가 각 파일 블록을 관리하는지 등과 같은 
  - 파일 시스템에 대한 메타데이터를 메모리에 보관
- 데이터 노드는
  -  파일 읽기 및 쓰기 파이프라인을 위해 서로 통신
- 파일은 
  - 블록으로 구성되며, 각 파일은 여러 차례 복제된다.
  -  이는 파일의 블록별로 동일한 복사본이 여러 개 있다는 뜻이다
- HDFS의 기능
  - 장애가 발생해도 데이터를 잃지 않는 견고성
  - 하드웨어 추가로 성능을 향상하는 확장성
  - 클러스터 내의 여러 노드에 대한 데이터 분할 등



![HDFS(Hadoop Distributed File System) 아키텍처](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F272BB24B531684C829)



#### Hive 란?

하둡 에코 시스템 중에서 <u>데이터를 모델링하고 프로세싱하는 경우</u> 가장 많이 사용하는 **데이터 웨어하우징용 솔루션**

RDB의 데이터베이스, 테이블과 같은 형태로 HDFS에 저장된 데이터 구조를 정의하는 방법을 제공

이 데이터를 대상으로 sql과 유사한 HiveQL 쿼리를 이용하여 데이터를 조회하는 방법 제공

![execute](https://wikidocs.net/images/page/23282/hive-hadoop-architecture.png)

- UI 
  - 사용자가 쿼리 및 기타 작업을 시스템에 제출하는 사용자 인터페이스
  - CLI, Beeline, JDBC 등
- Driver
  - 쿼리를 입력받고 작업을 처리
  - 사용자 세션을 구현하고, JDBC / ODBC 인터페이스 API 제공
- Compiler 
  - 메타 스토어를 참조하여 쿼리 구문을 분석하고 실행계획을 생성
- Metastore
  - 디비, 테이블, 파티션의 정보 저장
- Execution Engine
  - 컴파일러에 의해 생성된 실행 계획을 실행

##### 실행 순서

> spark sql
>
> : Hive 메타 스토어와 연결하여 Hive의 메타 정보를 이용하여 sql작업 처리 가능

1. 사용자가 제출한 SQL문을 드라이버가 컴파일러에 요청하여 메타스토어의 정보를 이용해 처리에 적합한 형태로 컴파일
2. 컴파일된 SQL을 실행엔진으로 실행
3. 리소스 매니저가 클러스터의 자원을 적절히 활용하여 실행
4. 실행 중 사용하는 원천데이터는 HDFS등의 저장장치를 이용
5. 실행결과를 사용자에게 반환







### 컴포넌트 구성

:one:**스파크 라이브러리**, :two:**스파크 코어**, :three:**클러스터 매니저**로 구분

![1.스파크? - 빅데이터 - 스칼라(scala), 스파크(spark)로 시작하기](https://lh3.googleusercontent.com/proxy/g71csBdFR2pQ8Llv5shOzYWfSH8JZahZ0cOdQtAP9uPsC8AtLlbRQBGNAP5NfiVeb7hIkQug03GXoFmYH4cj2NBQAJ8S3l6QvMOqNP4jr7rkfA)

#### 1️⃣ 스파크 라이브러리

스파크 라이브러리는 빅데이터 처리를 위한 작업용 라이브러리이다

스파크 공식 지원 라이브러리는 다음과 같다.

##### Spark SQL

- sql을 이용하여 RDD, Dataset, DataFrame 작업을 생성하고 처리
- Hive 메타 스토어와 연결하여 Hive의 메타 정보를 이용하여 sql작업 처리 가능
- 샤크(shark)는 Hive에서 스파크 작업을 처리할 수 있도록 개발하는 외부 프로젝트 → 현재는 spark sql로 통합

##### Spark Streaming

- 실시간 데이터 스트림을 처리하는 컴포넌트
- 스트림 데이터를 작은 사이즈로 쪼개어 RDD처럼 처리

##### MLib

- 스파크 기반의 머신러닝 기능 제공 컴포넌트
- 분류, 회귀, 클러스터링, 협업 필터링 등 머신러닝 알고리즘과 모델 평가 및 외부 데이터 불러오기 같은 기능도 지원

##### GraphX

- 분산형 그래프 프로세싱이 가능하게 해주는 컴포넌트
- 각 간선이나 점에 임의의 속성을 추가한 지향성 그래프 생성 가능



#### 2️⃣ 스파크 코어

spark core는 **메인 컴포넌트**로 

- 작업 스케줄링
- 메모리 관리
- 장애 복구

와 같은 **기본적인 기능 제공**하고, 

**RDD, Dataset, DataFrame을 이용한 스파크 연산을 처리**한다.

- **RDD** :스파크가 사용하는 **핵심 데이터 모델**로서 **다수의 서버에 걸쳐 분산 방식으로 저장된 데이터 요소들의 집합**을 의미하며, 병렬처리가 가능하고 장애가 발생할 경우에도 스스로 복구될 수 있는 내성을 가지고 있다.



#### 3️⃣클러스터 매니저

스파크 작업을 운영하는 클러스터 관리자

스파크는 다양한 클러스터 매니저를 지원

스파크에서 제공(지원)하는 관리자

-  Standalone 관리자
- Mesos 관리자
- YARN 관리자
- Kubernetes 관리자 등등



## 2. 스파크 구조

1. 작업을 관리하는 **드라이버**
2. 작업이 실행되는 노드를 관리하는 **클러스터 매니저**



### 스파크 애플리케이션의 구조

**실행**

마스터 - 슬레이브 구조 

**구성**

1. 작업을 관장하는 **드라이버**
   - 스파크 컨텍스트 객체를 생성하여 클러스터 매니저와 통신하면서 클러스터의 자원 관리를 지원
   - 애플리케이션의 라이프 사이클 관리
2. 실제 작업이 동장하는 **익스큐터**

![spark architecture](https://wikidocs.net/images/page/26630/cluster-overview.png)

### 스파크 애플리케이션

스파크 실행 프로그램으로 드라이버와 익스큐터 프로세스로 실행되는 프로그램

클러스터 매니저가 스파크 애플리케이션의 리소스를 효율적으로 배분한다.

#### 드라이버 (Driver)

- 스파크 애프리케이션을 실행하는 프로세스
- `main` 함수 실행
- 스파크 컨텍스트 객체 생성
- 스파크 라이프사이클 관리
- 사용자로부터 입력을 받아 애플리케이션에 전달
- 작업 처리 결과를 사용자에게 알려줌

실행 시점에 디플로이 모드 → 클라이언트 모드, 클러스터 모드로 설정 가능

- 디플로이 모드 
  - 설정 client : 프로그램을 실행하는 노드에서 드라이버 실행
  - 설정 cluster : 클러스터 내부의 노드에서 드라이버 실행

- 클라이언트 모드 : 클러스터 외부에서 드라이버 실행
- 클러스터 모드 : 클러스터 내부에서 드라이버 실행

#### 익스큐터 (Executor)

- 태스크 실행을 담당하는 에이전트
- 실제 작업을 진행하는 프로세스
- YARN의 컨테이너라고 볼 수 있다
- 태스크 단위로 작업을 실행, 결과를 드라이버에 알려줌
- 익스큐터 동작 중 오류 발생시, 다시 재작업을 진행

##### 태스크 (Task)

- 익스큐터에서 실행되는 실제 작업
- 익스큐터의 캐쉬를 공유하여 작업의 속도를 높일 수 있다.



### 스파크 잡의 구성

1. Job
2. Stage
3. Task

![spark-job](https://wikidocs.net/images/page/26630/job-stage-task.png)



#### 잡 (Job)

- 스파크 애플리케이션으로 제출된 작업

#### 스테이지 (Stage)

- 잡을 작업의 단위에 따라 구분한 것

#### 태스크 (Task)

- 익스큐터에서 실행되는 실제 작업
- 데이터를 읽거나, 필터링하는 실제 작업을 처리



### 클러스터 매니저

스파크는 여러 가지 클러스터 매니저를 지원

- YARN
  - 하둡 클러스터 매니저
  - 리소스 매니저, 노드 매니저로 구성
- Mesos
  - 동적 리소스 공유 및 격리를 사용하여 여러 소스의 워크로드를 처리
  - 아파치의 클러스터 매니저
  - 마스터와 슬레이브로 구성됨
- StandAlone
  - 스파크에서 자체적으로 제공하는 클러스터 매니저
  - 각 노드에서 하나의 익스큐터만 실행 가능



## 3. 스파크 모니터링

**방법**

1. 웹 UI 이용
2. REST API 이용

스파크 컨텍스트 웹 UI

- 스파크 컨텍스트가 실행되면 4040포트로 웹 UI를 실행
- 하나의 노드에 여러개의 컨텍스트가 실행되면 포트번호가 1씩 증가하면서 생성 (4041, 4042...)
- 스파크 컨텍스트가 실행되고 있는 동안에만 사용 가능

스파크 히스토리 서버

- 실행중인 작업과 실행이 끝난 작업의 히스토리를 확인하기 위한 서버
- `start-history-server.sh`로 실행하고 기본 접속 포트는 `18080`
- 영구적인 저장소에 스파크 작업 내용을 저장 하고 사용자의 요청에 정보를 반환



### 확인 가능 정보

- 스테이지와 태스크 목록
- RDD 크기와 메모리 사용량
- 환경변수 정보
- 익스큐터의 정보



### REST API

스파크 히스토리 서버는 작업 애플리케이션에 대해 REST API를 이용해 JSON 형태의 정보를 제공

```sql
curl -s http://$(hostname -f):18080/api/v1/applications
curl -s http://$(hostname -f):18080/api/v1/[app-id]/jobs
```



# 스파크 애플리케이션

- 실행 방법
- 구현 방법
- RDD
- 데이터 셋, 데이터 프레임, SQL



## 1. 실행 

스파크 애플리케이션은 스칼라, 자바, 파이썬, R로 구현 가능

각 언어로 스칼라 SQL 실행 가능

스파크 애플리케이션은 jar파일로 묶어서 실행하거나, REPL 환경에서 실행 가능



## 2. RDD, 데이터 셋, 데이터 프레임

스파크 애플리켕션 구현 방법

1. RDD 이용 방법

2. 데이터셋과 데이터프레임을 이용하는 방법 (RDD 단점 개선 방법)

![dataset, dataframe](https://i.stack.imgur.com/3rF6p.png)



### RDD

- RDD API를 이용하여 데이터 처리
- 장점 : 인메모리 데이터 처리를 통하여 처리 속도 높임
- 단점 : 테이블 조인 효율화 같은 처리를 사용자가 직업 제어 ⇒ 최적화에 어려움 발생

```sql
# RDD 예제 
val data = Array(1, 2, 3, 4, 5)
val distData = sc.parallelize(data)
distData.map(x => if(x >= 3) x else 0).reduce((x, y) => x + y)
```



### DataFrame

- 데이터프레임은 처리 속도 증가를 위한 프로젝트 텅스텐의 일부로 소개됨

- 데이터를 스키마 형태로 추상화

- 카탈리스트 옵티마이저가 쿼리를 최적화 하여 처리

```sql
# 데이터프레임 예제 
val df = spark.read.json("examples/src/main/resources/people.json")
df.select($"name", $"age").filter($"age" > 20).show()
df.groupBy("age").count().show()
```



### Dataset

- 데이터 처리 속도를 더욱 증가시켰다
  - 데이터의 타입체크
  - 데이터 직렬화를 위한 인코더
  - 카탈리스트 옵티마이저를 지원
- 데이터프레임과 데이터셋을 통합
- 스칼라 API에서 Dataset[Row]는 DataFrame 의미

```sql
# 데이터셋 예제 
val path = "examples/src/main/resources/people.json"
val peopleDS = spark.read.json(path).as[Person]
peopleDS.show()
```

![rdd,ds,df](https://databricks.com/wp-content/uploads/2016/06/Unified-Apache-Spark-2.0-API-1.png)

![rdd,dataset,dataframe](https://indatalabs.com/wp-content/uploads/2017/04/pic-2-742x403.png)

스파크 애플리케이션을 개발 할 때

- RDD는 스파크 컨텍스트를 이용
- 데이터셋, 데이터프레임은 스파크 세션 객체를 이용
  - 스파크 세션에서는 sql을 이용하여 데이터를 처리할 수도 있다.
- sql과 데이터셋, 데이터프레임을 이용한 처리는 동일한 엔진을 이용하기 때문에 사용자에게 편리한 API를 이용



## 3. RDD

RDD를 이용한 애플리케이션 처리 방법

스파크가 사용하는 **핵심 데이터 모델**로서 **다수의 서버에 걸쳐 분산 방식으로 저장된 데이터 요소들의 집합**

## 스파크 컨텍스트, RDD 초기화

RDD는

- 외부 데이터 읽어서 처리
- 자체적으로 컬렉션 데이터를 생성하여 처리 가능
- 데이터 처리는 파티션 단위로 분리하여 작업 처리

RDD의 연산 타입

1. 트랜스포메이션 (transformation)

   - 필터링 같은 작업

   - RDD에서 새로운 RDD를 반환

2. 액션 (action)

   - RDD로 작업을 처리하여 결과를 반환
   - 스파크는 지연 처리를 지원하여 트랜스포메이션을 호출할 때는 작업을 처리 하지 않고, 액션을 호출하는 시점에 작업을 처리하여 작업의 효율성을 제공

RDD는 액션이 실행될 때마다 새로운 연산을 처리

- 작업의 처리 결과를 재사용하고 싶으면 `persist()`메소드를 사용하여 결과를 메모리에 유지 가능

RDD는 스파크 컨텍스트 객체를 이용하여 생성 가능



### 스파크 컨텍스트 초기화

스파크 컨텍스트 객체는 `SparkConf` 객체를 이용해서 설정값을 생성하고, 초기화 가능

스파크 쉘을 이용할 경우 REPL쉘이 스파크 컨텍스트 객체를 생성

- 실행시, 스파크 컨텍스트와 스파크 세션을 생성했다는 메시지 확인 가능



### RDD 초기화

1. 내부 데이터 이용 방법
2. 외부 데이터 이용 방법

#### 내부 데이터 이용 (Parallelized Collections)

- 스파크 컨텍스트의 `parallelize()` 메소드 이용하여 처리
- 사용자가 직접 데이터를 입력하여 생산
- 생성한 객체는 RDD 타입
  - 해당 객체를 `map()` `reduce()` `filter()` 등의 RDD 연산을 이용하여 처리 가능



#### 외부 데이터 이용 

- 스파크 컨텍스트의 `textFile()` 메소드 이용하여 처리
- 스파크는 HDFS, S3, HBase 등 다양한 파일시스템 지원
- 생성한 객체는 RDD 타입이므로 RDD연산을 이용하여 처리 가능



## RDD 연산 (1)

**트랜스포메이션**

- RDD를 이용하여 새로운 RDD 생성

**액션**

- RDD 이용해서 작업 처리하여 결과를 드라이버에 반환하거나, 파일스스템에 결과를 쓰는 연산

스파크는 

- 트랜스포메이션을 호출할 때, 작업 구성
- 액션이 호출 될 때, 실제 계산 실행



### 트랜스포메이션(Transformations)

RDD를 이용하여 

- 데이터를 변환하고, 
- RDD를 반환하는 작업

**주요 함수**

- map() : 처리된 새로운 데이터셋 반환
- filter() : true를 반환한 값으로 필터링
- flatMap() : 배열을 반환하고, 이 배열들을 하나의 배열로 반환
- distince() 
- groupByKey()
- reduceByKey : 키를 기준으로 주어진 func로 처리된 작업 결과를 반환
- sortByKey()



### 액션(Actions)

RDD를 이용하여

- 작업을 처리한 결과르 반환하는 작업

**주요 함수**

- reduce() : 데이터를 집계(두 개의 인수를 받아서 하나를 반환). 병렬처리가 가능해야 함
- collect() : 처리 결과를 배열로 반환. 필터링 등 작은 데이터 집합을 반호나하는 데 유용
- count()
- first() : 데이터셋의 첫번째 아이템 반환 (take(1)과 유사)
- take(n) : 데이터셋의 첫번째 부터 n개의 배열을 반환
- saveAsTextFile()
- countByKey()
- foreach() : 데이터셋의 각 엘리먼트를 처리. 보통 accmulator와 함께 사용



### 함수 전달

RDD연산 처리 시, 매번 작업을 구현하지 않고

- 함수로 구현하여 작업 처리 가능



### 캐쉬 이용

RDD는 처리 결과를

- 메모리
- 디스크

에 저장하고 다음 계산에 이용 가능

작업의 종류와 영향을 파악한 후에 캐슁를 이용하는 것이 좋다.

- 반복작업의 경우, 캐쉬를 이용해서 처리 속도 높일 수 있다.

- 단일작업의 경우, 데이터 복사를 위한 오버헤드가 발생하여 처리시간이 더 느려질 수 있다.

RDD 캐슁 지원 메소드

- `persist()`
- `cache()`

캐슁한 데이터에 문제가 생기면 자동 복구

**저장 방법 설정 가능**

- 메모리, 디스크에 저장 가능
- 설정 종류
  - MEMORY_ONLY
  - MEMORY_AND_DISK
  - DISK_ONLY



## RDD 연산(2)

기본 연산외에 좀 더 복합적인 연산 처리 방법

### key, value를 이용한 처리

스파크는 맵리듀스 처럼 (key, value) 쌍을 이용한 처리 가능

기본적으로 제공하는 함수를 이용해서 좀 더 편리한 처리가 가능

- `flatMap` `reduceByKey`, `groupByKey`, `mapValues`, `sortByKey`

#### **예시**

워드 카운트는 키, 밸류를 이용한 처리 확인 가능

- 파일의 데이터를 읽음
- `flatMap` 이용하여 단어별로 분리
- `map` 이용하여 단어의 개수를 세어준다
- `reduceByKey` 를 이용하여 단어별로 그룹화 
- 단어가 나타난 개수를 센다

```sql
val txts = sc.textFile("/user/sample.txt")
val pairs = txts.flatMap(line => line.split(" ")).map(word => (word, 1))
val counts = pairs.reduceByKey(_ + _) 

scala> counts.take(10).foreach(println)
(under,1)                                                                     
(better.,1)
(goals,1)
(call,3)
(its,7)
(opening,1)
(extraordinary,1)
(internationalism，to,1)
(have,4)
(include,2)
```



### 어큐뮬레이터(Accmulator)

스파크는 pc단독 처리가 아닌 클러스터에서 처리

- 클로져 이용시 결과 달라질 수 있다.

`foreach()` 반복문에 외부에 선언된 변수에 함수를 실행하면 실행 모드(local, cluster)에 따라 결과가 달라질 수 있다.

스파크에서 Accumuator를 이용하여 

- 모든 노드가 공유할 수 있는 변수 선언해야 함

Accumuator 

- 맵리듀스의 카운터와 유사한 역할
- 스파크 컨텍스트를 이용해서 생성



### 브로드캐스트(broadcast)

모든 노드에서 공유되는 읽기 전용 값

- 맵리듀스의 디스트리뷰트 캐쉬(distribute cache)와 유사한 역할
- `broadcast()` 이용하여 사용 가능
- 조인에 이용되는 값들을 선언하여 이용



### 셔플

스파크에서 조인, 정렬 작업은 셔플 작업 실행

셔플은

- 파티션간에 그룹화된 데이터를 배포하는 메커니즘
- 많은 비용이 듬
  - 임시 파일의 복사, 이동이 있기 때문



# 스파크 스트리밍

실시간 데이터 분석은

- 페이지 뷰에 대한 통계 추적
- 머신러닝 모델 학습

로그 분석을 통해

- 실시간 에러 감지
- 현재 사용자의 구매 패턴 분석하여 물품 추천

**스파크 스트리밍**은 **실시간 데이터 분석을 위한 스파크의 컴포넌트**

- 디스트림
- 스트리밍 컨텍스트
- 스트리밍 워드 카운트
- 윈도우 트랜스포메이션
- 디스트림 연산

## 디스트림(DStream)

**스파크 스트리밍**은 **실시간 데이터 분석을 위한 스파크의 컴포넌트**

**데이터 입력**

- 카프카, 플럼, 키네시스, TCP, 소켓 등 다양한 경로를 통해 입력 받고

**데이터 분석**

- `map` `reduce` `window` 등이 연산을 통해 데이터를 분석

데이터 입력 / 분석하여 최종적으로 

- 파일 시스템 (FS)
- 데이터베이스 (DB) 등에 **적재된다.**

또한, 이 데이터를 

- 스파크의 머신러닝 (MLib)
- 그래프 컴포넌트 (GraphX) 에 **이용 가능**

![spark](https://spark.apache.org/docs/2.2.0/img/streaming-arch.png)

스파크 스트리밍은 실시간 데이터 스트림을 받아서 

데이터를 **디스트림**이라 불리는 추상화 개념의 작은 배치 단위로 나누고 

디스트림을 스파크 엔진으로 분석

- 디스트림(DStream, distretized stream, 이산 스트림)

![batch data](https://spark.apache.org/docs/2.2.0/img/streaming-flow.png)



### 디스트림

- 시간별로 도착한 데이터들의 연속적인 모임
- 각 디스트림은 시간별 RDD들의 집합으로 구성된다
- 플럼, 카프카, HDFS 등 다양한 원천으로 부터 디스트림을 입력 받을 수 있음

![dstream](https://spark.apache.org/docs/2.2.0/img/streaming-dstream.png)

디스트림은 RDD와 마찬가지로 두 가지 타입의 연산을 제공

1. 새로운 디스트림을 만들어 낼 수 있는 **트랜스포메이션 연산**
2. 외부 시스템에 데이터를 써주는 **출력 연산**

- 디스트림은 RDD와 동일한 연산 지원
- 실시간 분석을 위한 특별한 기능도 지원
  - 시간 관련이나 슬라이딩 윈도우



## 스트리밍 컨텍스트 초기화

디스트림은 스트리밍 컨텍스트를 이용하여 생성

스트리밍 컨텍스트는 

- 스파크 컨피그 객체
- 스파크 컨텍스트 객체를 이용해 초기화 가능

스트리밍 컨텍스트를 초기화 할 때는

- 디스트림의 처리 간격을 지정해야 함
  - 디스트림의 처리 간격 ⇒ 스트림의 배치 단위



### 스파크 컨피크 이용

`Sparkconf()`

이용 방법

- 스파크 컨텍스트나 스파크 세션 객체를 초기화할 때와 동일
- 스파크 컨피그에 설정 정보를 입력하고
- 이를 이용해서 초기화

```sql
import org.apache.spark._
import org.apache.spark.streaming._

val conf = new SparkConf().setMaster("yarn").setAppName("NetworkWordCount")
val ssc = new StreamingContext(conf, Seconds(1))    # 1초간격 배치 처리 
```



### 스파크 컨텍스트 이용

`StreamingContect()`

이미 스파크 컨텍스트 객체가 생성되어 있는 경우,

- 스파크 컨피그를 이용하지 않고
- 스파크 컨텍스트를 전달하는 방법으로 초기화 가능

스파크 쉘에서 스트리밍 컨텍스트를 이용할 때 사용 가능

```sql
import org.apache.spark._
import org.apache.spark.streaming._

# sc는 생성된 스파크 컨텍스트 객체 
val ssc = new StreamingContext(sc, Seconds(5))  # 5초간격 배치 처리
```



## 스트리밍 워드 카운트 예제

스파크 스트리밍이 동작 방식을 워드 카운트 예제를 통해 확인

스트리밍 워드 카운트는 

- 데이터의 입력을 네트워크로 받는 점 외에는 
- RDD를 이용한 워드 카운트 예제와 동일



### 스트리밍 워드 카운트

- 스트리밍 컨텍스트를 초기화 할 때 `Seconds(5)`를 전달하여 디스트림 처리 간격을 5초로 설정

- `socketTextStream`을 이용해서 텍스트 데이터를 전달한 IP, port에 접속하여 입력 받음
- 이 데이터를 워드 카운트 처리하고 `print`를 이용하여 화면에 출력합니다.

- `start`를 호출하면 소켓 텍스트 스트림을 이용하여 원격지에 접속하여 텍스트 스트림을 입력 받음
- `awaitTermination`을 이용하면 별도의 스레드로 작업을 시작하여 사용자의 세션이 끊어져도 계속 작업을 진행

```sql
import org.apache.spark._
import org.apache.spark.streaming._

val ssc = new StreamingContext(sc, Seconds(5))      # 5초간격 배치 처리 
val lines = ssc.socketTextStream("127.0.0.1", 9999) # 텍스트를 입력 받을 IP, port 입력 
val words = lines.flatMap(_.split(" "))
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)
wordCounts.print()

ssc.start()             # 데이터 받기 시작 
ssc.awaitTermination()  # 별도의 스레드로 작업 시작 
```



### 실행

위 예제의 실행은 

- 서버(netcat)  
  - 로그 데이터 전달을 위함
  - 넷캣을 이용
- 클라이언트(스파크 스트리밍)

를 실행하는 것으로 나눌 수 있다.



#### netcat 실행

`nc`명령을 다음과 같이 입력시 9999포트에서 TCP 입력을 대기한다. 연결되면 사용자 입력을 전달

```sql
# 9999 포트를 열어서 대기(listen)
$ nc -l 9999
a b c d a b c d a a a
```



### 스파크 스트리밍 실행

스파크 스트리밍은 위의 예제를 

- 스파크 서브밋(spark-submit)을 이용하여 제출해도 되고,
- 스파크 쉘(spark-shell)을 이용하여 실행해도 된다

**스파크 서브밋(spark-submit) 이용하는 경우**

- 위 예제를 입력하고 `start`를 호출하면 원격지에 접속하여 데이터를 전달 받고,
- 워드 카운트를 처리하여 데이터를 출력한다.

```sql
scala> ssc.start()    # 데이터 받기 시작 
-------------------------------------------
Time: 1548652935000 ms
-------------------------------------------
(d,2)
(b,2)
(a,5)
(c,2)
```

위와 같이 입력된 데이터를 시간 배치 간격으로 처리하여 출력

디스트림을 다음 처럼 시간 간격으로 처리

![stream](https://spark.apache.org/docs/2.2.0/img/streaming-dstream-ops.png)



## 윈도우 트랜스포메이션

디스트림의 트랜스포메이션 연산 2가지로 나눈다

1. 상태가 없는 연산 (stateless)
2. 상태를 가지는 연산 (stateful)

**상태가 없는 연산 (stateless)**

- 각 배치의 처리가 이전 배치의 데이터와 상관없이 진행
- `map`, `filter`, `reduce` 같은 일반적인 트랜스포메이션 연산

**상태를 가지는 연산 (stateful)**

- 이전 배치의 데이터나 중간 데이터를 이용하여 연산 처리
- 슬라이딩 윈도우와 시간별 상태를 추적하는 연산
- `updateStateByKey`, `reduceByWindow` 연산을 이용한 연산



### 체크 포인트

- 상태를 가지는 연산은 체크포인트 설정 해주어야 함
- 스트리밍 컨텍스트의 `checkpoint`를 이용하여 설정

```sql
ssc.checkpoint("/user/checkpoint/")
```

체크포인트를 설정하면 **윈도우 트랜스포메이션**의 중간계산 결과가 임시 데이터로 저장



### 윈도우 트랜스포메이션 (window transformation)

윈도우 연산은

- 여러 배치들의 결과를 합쳐서 
- 디스트림 배치 간격보다 훨씬 긴시간 간격에 대한 결과 계산

모든 윈도우 연산은 

- 윈도우 시간(window duration)과 
  - 윈도우 시간 : 처리에 필요한 시간의 개수
- 슬라이딩 시간(sliding duration)을 필요로 하며,
  - 슬라이팅 시간 : 처리 시간 간격
- 이 두가지 값은 모두 디스트림 배치 간격의 배수여야 함

![window](https://spark.apache.org/docs/2.2.0/img/streaming-dstream-window.png)

- 위 그림에서 윈도우 시간은 3, 슬라이딩 시간은 2
- 윈도우 시간 : 처리에 필요한 시간의 개수
- 슬라이딩 시간 : 처리 시간 간격



### 윈도우 트랜스포메이션 예제

`reduceByKeyAndWindow`를 이용한 윈도우 연산

- 스트리밍 워드 카운트와 동일한 연산을 처리하고, 
- 윈도우 연산을 위한 단계가 하나더 추가 

윈도우에 들어가는 배치를 위한 계산과, 

위도우에서 벗어나는 배치를 위한 연산을 추가하고, 

윈도우 시간과 슬라이딩 시간 간격을 입력하면 처리할 수 있습니다.

```sql
import org.apache.spark._
import org.apache.spark.streaming._

val ssc = new StreamingContext(sc, Seconds(5))
val lines = ssc.socketTextStream("1.1.1.1", 9999)
val words = lines.flatMap(_.split(" "))
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)

# 체크 포인트 설정 
ssc.checkpoint("/user/checkpoint")
# 윈도우 트랜스포메이션 설정 
val wordCountWindow = wordCounts.reduceByKeyAndWindow( 
    {(x, y) => x + y}, # 윈도에 들어가는 새로운 배치들의 계산 
    {(x, y) => x - y}, # 윈도에서 벗어나는 범위의 값을 계산 
    Seconds(30), # 윈도우 시간 
    Seconds(10)  # 슬라이딩 시간 
)
wordCountWindow.print()

ssc.start()
ssc.awaitTermination()
```



### 실행

- 스트리밍 윈도우 예제를 실행하고 넷캣(서버)을 이용하여 다음과 같이 실행

```sql
$ nc -l 9999
a b c d a b c d a a a
a b c d a b c d a a a
```



스트리밍 윈도우 다음과 같이 처리

- 데이터 처리 간격(슬라이딩 시간) : 10초
- 윈도우 시간 간격(처리에 필요한 시간의 개수) : 30초
- 30초 전의 데이터를 이용해서 10초 마다 데이터 처리

```sql
scala> ssc.start()    # 데이터 받기 시작 
```



## 디스트림 연산

디스트림 연산은 이전에 살펴 본 연산들 이용 가능

- 트랜스포메이션 연산
- 윈도우 연산 외에 조인
- 유니온 연산
- 출력 연산 



### 조인, 유니온 연산

스트림의 조인과 유니온 연산도 쉽게 처리 가능

- 스트림 끼리의 연산은

  - `join` 
  - `leftOuterJoin`
  -  `rightOuterJoin`
  -  `fullOuterJoin`
  -  `union` 연산

  이용해서 처리 가능



#### 디스트림간의 연산

```sql
val stream1: DStream[String, String] = ...
val stream2: DStream[String, String] = ...
val joinedStream = stream1.join(stream2)
```

- 조인의 윈도우 연산도 쉽게 처리 가능
- 다음과 같이 `window`를 이용하여 시간 간격 입력 

```sql
val windowedStream1 = stream1.window(Seconds(20))
val windowedStream2 = stream2.window(Minutes(1))
val joinedStream = windowedStream1.join(windowedStream2)
```



#### 조인 연산 예제

```sql
import org.apache.spark._
import org.apache.spark.streaming._

val ssc = new StreamingContext(sc, Seconds(5))
val lines1 = ssc.socketTextStream("1.1.1.1", 9999)
val wordCounts1 = lines1.flatMap(_.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)

val lines2 = ssc.socketTextStream("1.1.1.1", 9998)
val wordCounts2 = lines2.flatMap(_.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)

val unionStream = wordCounts1.union(wordCounts2)
unionStream.print()

ssc.start()
```



#### RDD와 디스트림간 연산

RDD와 디스트림간의 연산도 `transform`을 이용해서 처리 가능

```sql
val dataset: RDD[String, String] = ...
val windowedStream = stream.window(Seconds(20))...
val joinedStream = windowedStream.transform { rdd => rdd.join(dataset) }
```



### 출력 연산

디스트림 연산의 결과는 

- 출력 연산을 이용해서 
- 파일시스템이나
- 데이터베이스에 외부 저장소에 저장할 수 있음

**함수**

- print() : 디스트림 배치의 데이터에서 10개 출력. 디버그용
- saveAsTextFiles 
- saveAsObjectFiles: 디스트림 배치의 데이터를 시퀀스 파일로 저장
- saveAsHadoopFiles 
- foreachRDD : 디스트림에 함수를 적용하여 RDD를 생성하고 이를 출력하는 범용적인 출력 연산. 주어진 함수는 외부 시스템에 데이터를 쓰는 함수



### 파일 저장

파일을 저장하는 함수는

- 저장할 디렉토리와 접미어를 파라미터로 받음
- 각 배치의 결과는 
  - 주어진 디렉토리 아래 저장되고 
  - 저장시간과 접미어가 폴더명으로 생성

```sql
wordCounts.saveAsTextFiles("/user/stream/txt_data", "txt")
```

파일로 저장하면 다음과 같이

- 주어진 폴더명으로 디렉토리를 생성하고,

- 시간대별로 폴더를 생성하여 데이터를 저장



### foreachRDD를 이용한 범용 연산

`foreachRDD`를 이용한 연산은 

- RDD의 모든 연산을 사용 가능
- 이를 이용해서 외부 DB에 데이터를 저장할 수 있다.

```sql
dstream.foreachRDD { rdd =>
  val connection = createNewConnection()  // executed at the driver
  rdd.foreach { record =>
    connection.send(record) // executed at the worker
  }
}
```

