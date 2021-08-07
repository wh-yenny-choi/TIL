# JOIN

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