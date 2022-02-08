# 4장

> ## 스파크 API 깊이 파헤치기

학습 내용

- 키-값 쌍을 다루는 방법
- 데이터 파티셔닝와 셔플링
- 그루핑, 정렬, 조인 연산
- 누적 변수와 공유 변수를 사용하는 방법



### 🧠 알아둘 것

RDD

DataFrame

- RDD보다 더 큰 개념
- 데이터 다루는 단위

DataSet

- 진화중



++ 가상 머신 종료

`$ vagrant halt` : halt명령으로 가상 머신 중지해도 작업 내용 보존

- 가상 머신 저장 종료하고 싶을때

`$ vagrant destory` : 가상 머신을 완전히 제거하고 디스크의 여유 공간을 확보

`$ vagrant box remove manning/spark-in-action` : 가상 머신 생성하는 데 사용한 베이그런트 박스 파일 삭제 명령어





## 4.1 Pair RDD 다루기

### 4.1.1 

스파크에서는 키-값으로 구성된 RDD를 Pair RDD라고 함

#### 4.1.2.4

mapValues 변환 연산자로 pair RDD 값 바꾸기 실습

```
#section 4.1.2
val tranFile = sc.textFile("first-edition/ch04/"+"ch04_data_transactions.txt")
val tranData = tranFile.map(_.split("#"))
val transByCust = tranData.map(tran => (tran(2).toInt, tran))


# 4.1.2.1 키 및 값 가져오기
transByCust.keys.distinct().count()

# 4.1.2.2 키별 개수 세기
transByCust.countByKey()
transByCust.countByKey().values.sum
val (cid, purch) = transByCust.countByKey().toSeq.sortBy(_._2).last
val complTrans = Array(Array("2015-03-30", "11:59 PM", "53", "4", "1", "0.00"))

# 4.1.2.3 단일 키로 값 찾기
transByCust.lookup(53)
transByCust.lookup(53).foreach(tran => println(tran.mkString(", ")))

# 4.1.2.4 mapValues 변환 연산자로 Pair RDD값 바꾸기
transByCust = transByCust.mapValues(tran => { 
if(tran(3).toInt == 25 && tran(4).toDouble > 1)
tran(5) = (tran(5).toDouble * 0.95).toString
tran })

```



## 4.2 데이터 파티셔닝을 이해하고 데이터 셔플링 최소화



## 4.3 데이터 조인, 정렬, 그루핑

### 4.3.1 데이터 조인

다양한 변환 연산자를 사용하여 RDD를 다른 RDD와 결합할 수 있다. (RDD내용 합치기 가능)

- 변환 연산자 : `zip`, `cartesain`, `intersection`

조인 연산자

- leftouter join
- rightouter join
- fullouter join



>  **📌숙제  조인 정리**



```
transByProd = transByCust.map(lambda ct: (int(ct[1][3]), ct[1]))
totalsByProd = transByProd.mapValues(lambda t: float(t[5])).reduceByKey(lambda tot1, tot2: tot1 + tot2)

products = sc.textFile("/pathto/ch04_data_products.txt").map(lambda line: line.split("#")).map(lambda p: (int(p[0]), p))
```





#### 4.3.1.1. RDBMS와 유사한 조인 연산자

```
totalsAndProds = totalsByProd.join(products)
totalsAndProds.first()

totalsWithMissingProds = products.leftOuterJoin(totalsByProd)
missingProds = totalsWithMissingProds.filter(lambda x: x[1][1] is None).map(lambda x: x[1][0])
from __future__ import print_function
missingProds.foreach(lambda p: print(", ".join(p)))
```





#### 4.3.1.2 subtract나 subtractByKey 변환 연산자로 공통 값 제거

```
missingProds = products.subtractByKey(totalsByProd)
missingProds.foreach(lambda p: print(", ".join(p[1])))
```





#### 4.3.1.3 cogroup 변환 연산자로 RDD 조인

```
prodTotCogroup = totalsByProd.cogroup(products)
prodTotCogroup.filter(lambda x: len(x[1][0].data) == 0).foreach(lambda x: print(", ".join(x[1][1].data[0])))
totalsAndProds = prodTotCogroup.filter(lambda x: len(x[1][0].data)>0).\
map(lambda x: (int(x[1][1].data[0][0]),(x[1][0].data[0], x[1][1].data[0])))
```





#### 4.3.1.4 intersection 변환 연산자 사용

```
totalsByProd.map(lambda t: t[0]).intersection(products.map(lambda p: p[0]))
```



#### 4.3.1.5 cartensian 변환 연산자로 RDD 두 개 결합

```
rdd1 = sc.parallelize([7,8,9])
rdd2 = sc.parallelize([1,2,3])
rdd1.cartesian(rdd2).collect()
rdd1.cartesian(rdd2).filter(lambda el: el[0] % el[1] == 0).collect()
```



#### 4.3.1.6 zip 변환 연산자로 RDD 조인

```
rdd1 = sc.parallelize([1,2,3])
rdd2 = sc.parallelize([2,3,4])
rdd1.intersection(rdd2).collect()
```



#### 4.3.1.7 zipPartitions 변환 연산자로 RDD 조인 

```
missing = transByProd.subtractByKey(products)

rdd1 = sc.parallelize([1,2,3])
rdd2 = sc.parallelize(["n4","n5","n6"])
rdd1.zip(rdd2).collect()
```



### 4.3.2 데이터 정렬

137~ 153

```
#section 4.3.2
sortedProds = totalsAndProds.sortBy(lambda t: t[1][1][1])
sortedProds.collect()
```





### 4.3.3 데이터 그루핑

```
#section 4.3.3
def createComb(t):
    total = float(t[5])
    q = int(t[4])
    return (total/q, total/q, q, total)
def mergeVal((mn,mx,c,tot),t):
    total = float(t[5])
    q = int(t[4])
    return (min(mn,total/q),max(mx,total/q),c+q,tot+total)
def mergeComb((mn1,mx1,c1,tot1),(mn2,mx2,c2,tot2)):
         return (min(mn1,mn1),max(mx1,mx2),c1+c2,tot1+tot2)
avgByCust = transByCust.combineByKey(createComb, mergeVal, mergeComb).\
mapValues(lambda (mn,mx,cnt,tot): (mn,mx,cnt,tot,tot/cnt))
avgByCust.first()

totalsAndProds.map(lambda p: p[1]).map(lambda x: ", ".join(x[1])+", "+str(x[0])).saveAsTextFile("/destination")
avgByCust.map(lambda (pid, (mn, mx, cnt, tot, avg)): "%d#%.2f#%.2f#%d#%.2f#%.2f" % (pid, mn, mx, cnt, tot, avg)).saveAsTextFile("/destination")
```



## 4.4 RDD 의존 관계





## 4.5 누적 변수와 공유 변수





## 4.6 요약

- Pair RDD는 키와 값 튜플로 구성된 RDD다
- 스파크의 데이터 파티셔닝은 데이터를 여러 클러스터 노드로 분할하는 메커니즘
  - 파티셔닝 : 대용량의 테이블이나 인덱스를 작은 논리적 단위인 파티션으로 나누는 것
    - 파티셔닝 이유? ⇒ **성능을 위해서**
  - 클러스터 : 큰 범위로 보면, 여러 서버가 네트워크로 연결된 상태
    - 클러스터는 데이터 저장 시 데이터 액세스 효율을 향상시키기 위해 **동일한 성격의 데이터를 동일한 데이터 블록에 저장**하는 물리적 저장 방법이다.
    -  클러스터링키로 지정된 컬럼 값의 순서대로 저장되고, 여러 개의 테이블이 하나의 클러스터에 저장된다.

- 스파크의 조인 연산자는 이름이 같은 RDBMS 조인 연산자 (join, leftouter join, rightouter join, fullouter join)와 동일하게 동작
- 스파크에서는 aggregateByKey, groupByKey(또는 groupBy), combineByKey 등 다양한 Pair RDD변환 연산자로 데이터를 그루핑 할 수 있다.



> **시간이 많이 지난 상품권 사용가능할까?** 

백화점은 상품권 시리얼 번호(데이터) 소유

수 많은 데이터 존재

- 여러 디스크에 년도별로 파티셔닝해서 소유 ⇒ **아카이빙**

  - 디지털 아카이빙 : 다지털 정보 자원을 장기적으로 보존하기 위한 작업
    - 아날로그 콘텐츠는 디지털로 변환한 후 압축하여 저장하고, 디지털 콘텐츠도 체계적으로 분류하고 메타 데이터를 만들어 DB화하는 작업

  - 디지털 아카이빙은 늘어나는 정보 자원의 효율적인 관리와 이용을 위해 필요한 작업

사용시 해당 년도의 디스크를 확인 후 검색 ⇒ **파티셔닝**