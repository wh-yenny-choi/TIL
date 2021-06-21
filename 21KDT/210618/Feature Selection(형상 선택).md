# Feature Selection(형상 선택)

## 형상 선택 기법

![image-20210621112324086](Feature Selection(형상 선택).assets/image-20210621112324086.png)

위 그림에서 Dimensionality Reduction은 PCA라고 가정

- PCA는 목표변수가 없다 (= y값이 없다)
- 2차원 이상의 데이터 분포에서 차원을 축소하면서 축을 찾는것
- overfiting사용 X
- pca 고유값은 feature개수만큼 나온다.

https://towardsdatascience.com/pca-clearly-explained-how-when-why-to-use-it-and-feature-importance-a-guide-in-python-7c274582c37e



### supervised running

supervised running에서는 y값을 넣음(목표 변수값 넣음)

- 회귀 FS (regression feature selection)

#### Wrapper Methonds

 wrapper는 예측 모델을 사용하여 피처들의 부분 집합을 만들어 계속 테스트 하여 최적화된 피처들의 집합 만드는 방법. 즉, Wrapper Method는 예측 정확도 측면에서 가장 좋은 성능(performance)을 보이는 feature subset(피처 집합)을 뽑아내는 방법

##### RFE (Recursive Feature Elimination)

Feature Selection의 supervised의 Wrapper Methonds방식인 RFE

+ scikit-learn 함수
+ SVM을 사용하여 재귀적으로 제거하는 방법
+ 유사한 방법으로 Backward Elimination, Forward Elimination, Bidirectional elimiation이 있다.



```sql
from sklearn.feature_selection import RFE
#from sklearn.tree import DecisionTreeClassifier  변수가 0 or 1일때 사용
from sklearn.svm import SVR
estimator = SVR(kernel='linear')  #tip -> linear
rfe = RFE(estimator, n_features_to_select=4)
selector = rfe.fit(data_trans, y)   #fit에 매개변수
```

- 코드에서 DecisionTreeClassifier를 사용하면 Kendall's 확인

- RFE는 fit할때(모델 피팅 할때), 목표변수 y가 들어간다.



**참고**

input variable  **Numerical**

- output variable 
  - **Numerical( - Pearson's , Spearman's)**
  - **Categorical( - ANOVA, Kendall's)**
    - 카테고리형 변수 - 중앙값 또는 최빈값 주기

![image-20210621112304664](Feature Selection(형상 선택).assets/image-20210621112304664.png)

**<u>RFE의</u>** 

- input variable 은 **Numerical( - Pearson's)**
-  output variable **Categorical( - Kendall's)**

RFE에서 y값(tip)이 classifier(변수가 0 or 1)`categorical`임.  

따라서 **kendall's**로 확인해야 하는데 <u>target variable(tip, y, output variance)이 Categorical이 아니라Numerical</u> `regression`

따라서,  <u>강제로 SVM을 사용</u>하여 **Classifier가 아닌 estimator로 진행**

- estimator`Numerical` = SVR(kernel='linear'`categorical`)  #tip -> linear 강제로 변경
  - categorical가 아닌 target variable을 SVR(도구?)사용하여 emtimator`Numerical`로 정의
- tip은 0 과 1로 구분되어지지 않음 => categorical (X) Numerical(O)



### Regression Feature Selection

Regression Feature Selection은 supervised running. 즉, 목표 변수 가진다.

Regression FS의 Target variable은 Numerical

파생변수(mutate variable) 사용

output variable이 regression(Numerical)이면 profile_report()에서 Pearson's 확인

output variabl이 classification(categorical)이면 profile_report()에서 Kendall's 확인

```sql
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
```





## PCA와 RFE 수업 중 질문 정리

1.

pca는 형상 추출(FE) 방법, rfe는 형상 선택 방법(FS) 중 하나인 wrapper method 방법 중 하나

- pca 는 독립변수(input variable, feature)들끼리의 상관관계만으로만 차원을 축소시키고 

- rfe는 종속변수(output variable)들과 목표변수(target variable)와의 관계를 통해 차원을 축소시킨다
  - 목표변수 - 수업에서는 y로 설정

2.

목표변수는 Supervised에서 나오는데 supervised는 Feature Selection내에 존재. 즉, PCA는 목표변수와 상관 없다.

- pca는 목표변수 상관없이 순위 정함
- rfe는  목표변수를 어떤것으로 설정하느냐에 따라 우선순위가 바뀐다.

3.

 profile_report는 컬럼(feature)간 correlation을 분석하는거고, pca는 각 개체의 고유값을 표시하는건데 pca 결과값을 어떻게 profile_report로 분석할 수 있나요?

- 피어슨 상관계수는 두 feature간 관계를 보는것  → 상관성

- pca는 feature들 간에 모델에서의 영향력(크기)을 보는 것 → 크키
  - 다차원 공간에서의 영향력을 보는것 (힘의 크기)
  - pca용도 : 차원축소

- correlation은 힘의 크기와는 상관 X

예를 들면, 

- 주차장과의 매출의 상관성 (Peason's)

- 벡터 공간(방향)에서의 영향력 (PCA)

4.

각 Eigenvalue(고유값)의 피어슨 상관계수는 0이라고 나오는 이유?

- pca로 새로 축을 생성할 때 orthogonal(직교)하게 해서 상관이 0이  나오는 것
- pca는 크기만을 보기때문에 직교하므로 correlation이나오지 않음 
  - 다중공선성과는 상관 없다.

5.

profiling찍는 이유?

1. 목표변수(target variable)와 feature들간의 correlation 봐야함 (상관관계,인과관계) 

2. 큰 (많은) 다중공선성 제거하기 위해 

6.

pca와 상관계수 차이?

**데이터의 분산관점**에서 차원 축소는 pca(FE), **상관관계 관점**에서 차원 축소(FS)는 다중공선성 제거 (피어슨 등...) 

차원 축소의 관점이 다르다.

- pca는 corrvariance(공분산), variance(분산) 이용
- 상관계수는 모델을 계속 만들고, 결과를 비교한다. 예측력에 도움되는 feature와 parameter를 찾아 나가는 것





## 형상 선택 방법

![image-20210621112346030](Feature Selection(형상 선택).assets/image-20210621112346030.png)

### **Input variable(입력 변수)**

1. **Numerical **
2. **Categorical**



- 입력변수(input variable) = **독립변수(Independent variable)** = 특징(feature,기계학습에서) = Regressor(회귀자) = 조작변수(manipulated variable)
- 독립변수(Independent variable)
  - 일정하게 전제된 원인을 가져다 주는 기능을 하는 변수
  - 한 변수의 값의 변화가 다른 변수의 값의 변화에 영향을 미치는 변수

<u>현재 과정에서는 input variable이 numerical인것만 고려</u>



### output variable(출력 변수)

- 출력변수(output variable) = **Dependent variable(종속변수)** = Target variable(목표변수) = Response variable(반응 변수)

- 종속변수(Dependent variable)
  - 독립변수(입력변수)의 원인(영향)을 받아 일정하게 전제된 결과를 나타내는 기능을 하는 변수

#### Numerical output variable

##### Pearson's

변수간 상관관계를 가지고 featuring하는 방법

여러 feature들 간 데이터를 봤을때, 하나의 input parameter에서 분포의 크기를 무시할 수 없는 것을 선택

- 예를 들어,

아래의 그림은 pearson's 상관계수

![image-20210621113257114](Feature Selection(형상 선택).assets/image-20210621113257114.png)

피어슨 상관계수에서 팁과 성별을 볼 때, 

- 상관성이 없다.

목표변수가 totlabill일 때, **다중공선성 제거**시

- tip과 size 중 하나는 제거 할 수 있다. 

- day, time(, sex) 에서도 제거할 수 있다.

- 모델 만들때 (피팅할때), 다중공선성을 가지는 둘 중 하나는 평균을 내서 하나만 선택하여 차원을 축소

직관적으로 볼 때,  total_bill 등의 7개의 feature들과 tip _rate는 확연히 다르다.

- 차원 축소시(다중공선성 제거시),tip_rate는 상위에서 살아 남을것

비슷한 상관계수들은 제거하고, 새로운 신선한 feature을 선택하는 것 

- 차원 축소의 목적

차원 축소 => 정보 손실도 발생

모델에 넣고 결과값을 비교

모델을 계속 만들고, 예측력에 도움이 되는 feature와 parameter를 찾아 나가는 것 

mutate variable = 파생 변수 

modeling = parameter



##### Spearman's

input variable : Numerical

- output variable : Numerical



#### Categorical output variable

##### ANOVA

input variable : Numerical

- output variable : Categorical



##### Kendall's

input variable : Numerical

- output variable : Categorical



+) 

입력변수(input variable) = **독립변수(Independent variable)** = 특징(feature,기계학습에서) = Regressor(회귀자) = 조작변수(manipulated variable)

출력변수(output variable) = **Dependent variable(종속변수)** = Target variable(목표변수) = Response variable(반응 변수)

