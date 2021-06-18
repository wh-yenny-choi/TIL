# PCA(주성분)

**주성분 분석(PCA**, Principal Component Analysis**)**은 가장 대표적인 차원 축소 알고리즘이다. PCA는 먼저 데이터에 가장 가까운 초평면(hyperplane)을 구한 다음, 데이터를 이 초평면에 투영(projection)시킨다.

## 분산보존

저차원의 초평면에 데이터를 투영하기 전에 먼저 적절한 초평면을 선택해야 한다. PCA는 데이터의 분산이 최대가 되는 축을 찾는다. 즉, 원본 데이터셋과 투영된 데이터셋 간의 **평균제곱거리**를 **최소화** 하는 축을 찾는다. 아래의 그림에서 왼쪽 2차원 데이터셋을 오른쪽 그림처럼 투영했을 때 C<sub>1</sub>축으로 투영한 데이터가 분산이 최대로 보존되는 것을 확인할 수 있다.

![image-20210618091939910](C:\Users\ftsv2\TIL\21KDT\210617\할거.assets\image-20210618091939910.png)

## 주성분

**PCA단계**

1. 학습 데이터셋에서 분산이 최대인 축(axis)찾는다.
2. 이렇게 찾은 첫번째 축과 직교하면서 분산이 최대한 두 번째 축(axis)을 찾는다.
3. 첫번째 축과 두 번째 축에 직교하고 분산을 최대한 보존하는 세 번째 축을 찾는다.
4. 1~3번과 같은 방법으로 데이터셋의 차원(feature수, 특성 수) 만큼의 축(axis)을 찾는다

이렇게 `i`번째 축을 정의하는 **단위 벡터**(unit vector)를  `i`번째 **주성분**(PC, Principal Component)이라고 한다.

예를들어,  2차원 데이터셋에서 PCA는 분산을 최대로 보존하는 단위벡터 C<sub>1</sub>이 구성하는 축과 이 축에 직교하는 C<sub>2</sub>가 구성하는 축을 찾게 된다. 



## PCA구하는 과정

### 공분산(Covariance)

먼저, 주성분(PC)를 구하기 위해서는 공분산에 대해 알아야 한다. **공분산(covariance)**은 2개의 특성(또는 변수, Feature)간의 상관정도를 나타낸 값이다. 

예를들어, 아래의 그림과 같이 X,Y 두 개의 특성(Feature)에 대해 공분산을 구하면 다음과 같다.

![image-20210618092416987](C:\Users\ftsv2\TIL\21KDT\210617\할거.assets\image-20210618092416987.png)

![image-20210618092447837](C:\Users\ftsv2\TIL\21KDT\210617\할거.assets\image-20210618092447837.png)

### PCA 계산

PCA의 목적은 원 데이터(original data)의 분산을 최대한 보존하는 축을 찾아 투영(projection)하는 것이다.

공분산 C의 고유벡터 (eigenvector) e 

공분산 C의 고유값(eigenvalue) λ 

λ(고유값)는 eigenvector(고유벡터)로 투영했을 떄의 분산(variance)이다.

이때, 고유벡터의 열벡터를 주성분(PC, principal component)라고 한다.

따라서, 고유벡터(digenvector)에 투영하는 것이 분산이 최대가 된다.



## Scikit-Learn에서의 PCA계산

Scikit-Learn에서는 PCA를 계산할 때, 데이터셋에 대한 공분산의 **고유값 분해(eigenvalue-decomposition)**이 아닌 **특이값 분해(SVD, Singular Value Decomposition)**를 이용해 계산한다.



## Explained Variance Ratio 와 적절한 차원 수 선택하기

**Explained Variance Ratio**은 각각의 주성분 벡터가 이루는 축에 투영(projection)한 결과의 분산의 비율을 말하며, 각 **eigenvalue(고유값)**의 비율과 같은 의미이다.



## 압축을 위한 PCA

데이터셋의 차원을 축소하게 되면 데이터셋의 크기가 줄어든다.

![image-20210618093807152](C:\Users\ftsv2\TIL\21KDT\210617\할거.assets\image-20210618093807152.png)

PCA 적용결과 총 784 차원에서 154로 80%정도 차원이 축소된 것을 알 수 있다. 이러한 압축한 데이터셋을 이용해 SVM과 같은 분류알고리즘을 학습 시킬 경우 학습 속도를 빠르게 할 수 있다.

또한, 압축된 데이터셋에 PCA 투영 변환을 반대로 적용하여 다시 원 데이터의 차원(위의 경우 784)로 복원할 수 있다. 위에서 `5%` 만큼의 정보(분산)을 잃었기 때문에 완벽하게 복원은 할 수 없지만, 원본 데이터와 비슷하게 복원할 수 있다. 이러한 원본 데이터와 복원한 데이터간의 평균 제곱 거리를 **재구성 오차**(reconstruction error)라고 한다.



## Incremental PCA (IPCA)

PCA의 단점은 SVD(scikit-learn에서)를 수행하기 위해서는 전체 학습 데이터셋을 메모리에 올려야 한다는 것이다. 이러한 단점을 보완하기 위해 **Incremental PCA(IPCA)** 알고리즘이 개발되었다. 

IPCA는 학습 데이터셋을 미니배치로 나눈 뒤 IPCA 알고리즘에 하나의 미니배치를 입력으로 넣어준다. IPCA는 학습 데이터셋이 클때 유용하다.