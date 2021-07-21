#!/usr/bin/env python
# coding: utf-8

# # 사이킷런을 이용한 머신러닝

# - 파이썬 머신러닝 라이브러리 중 가장 많이 사용되는 라이브러리
# - 파이썬스러운 API
#     - 파이썬 기반의 다른 머신러닝 패키지도 사이킷런 스타일API 지향
# - 머신러닝을 위한 다양한 알고리즘 개발을 위해 편리한 프레임워크와 API 제공
# - 오랜 기간 실전 환경에서 검증, 매우 많은 환경에서 사용된 라이브러리
# 
# 
# ![image.png](attachment:image.png)
# 
# https://scikit-learn.org/stable/

# In[1]:


# 사이킷런 버전 확인
import sklearn
print(sklearn.__version__)

# Anaconda 설치기 기본으로 사이킷런 설치됨

# 설치 명령어
conda install scikit-learn

# 또는
pip install scikit-learn
# ## 사이킷런을 이용한 붓꽃(iris) 데이터 분류
# 
# - 붓꽃 데이터 세트를 사용해서
# - 붓꽃의 품종을 분류(Classification)
# 
# ### 붓꽃 데이터 세트
# - sklearn.datasets에 들어 있음
# - load_iris()를 통해 로드해서 사용
# - 머신러닝 각 분야에서 알고리즘을 측정하기 위한 기본 자료로 다양하게 활용
# - 4가지 속성(피처)을 가진 3가지 붓꽃 품종의 50개 샘플 포함
# 
# **3가지 붓꽃 품종**
# - Setosa
# - Versicolor
# - Virginica
# 
# ![image-2.png](attachment:image-2.png)
# http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

# ### 붓꽃의 4가지 속성(피처 (Feature))
# - 꽃받침 길이 : Sepal Length
# - 꽃받침 너비 : Sepal Width
# - 꽃잎의 길이 : Petal Length
# - 꽃잎의 너비 : Petal Width
# 
# 
# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ### 분류를 위한 학습 및 예측 프로세스
# 
# - 0단계. 데이터 세트 준비
#     - 데이터 세트 로딩, 데이터 프레임으로 변환
# 
# 
# - 1단계. 데이터 세트 분리
#     - 데이터를 학습 데이터와 테스트 데이터로 분리
# 
# 
# - 2단계. 모델 학습
#     - 학습 데이터를 기반으로 ML 알고리즘을 적용해 모델 학습
# 
# 
# - 3단계. 예측 수행
#     - 학습된 ML 모델을 이용해 테스트 데이터의 분류(붓꽃 종류) 예측
# 
# 
# - 4단계. 모델 성능 평가
#     - 예측된 결과값과 테스트 데이터 실제 값 비교하여 ML 모델 성능 평가
# 
# ![image.png](attachment:image.png)
#     

# 용어 정리
# 
# 피처(Feature) : 데이터 세트 속성
# - feature_names : sepal length, sepal with, petal length, petal width
#     
# 레이블(label) :
# - 품종 (setosa, versicolor, virginica)
# - 학습 : 결정값(주어진 정답)
# - 테스트 : 타깃값(target)(예측해야 할 값)
# - target(숫자) : 0, 1, 2
# - target_names : setosa, versicolor, virginica
# - 레이블 = 결정값 = 타겟값

# **붓꽃 예측을 위한 사이킷런 필요 모듈 로딩**

# In[2]:


from sklearn.datasets import load_iris  
from sklearn.tree import DecisionTreeClassifier  
from sklearn.model_selection import train_test_split


# - 사이킷런 패키지 모듈
#     * 명명규칙 : 모듈명은 sklearn으로 시작
#     * sklearn.datasets : 사이킷런에서 자체적으로 제공하는 데이터 세트를 생성하는 모듈 모임
#     * sklearn.tree : 트리 기반 ML 알고리즘을 구현한 클래스 모임
#     * sklearn.model_selection : 학습 데이터와 검증 데이터, 예측 데이터로 데이터를 분리하거나 최적의 하이퍼 파라미터로 평가하기 위한 다양한 모듈의 모임

# **붓꽃 데이터 예측 프로세스에서 사용하는 함수 및 클래스**
# * load_iris() 함수 : 붓꽃 데이터 세트
# * DecisionTreeClassifier 클래스  : ML 알고리즘은 의사결정 트리 알고리즘 이용
# * train_test_split() 함수 : 데이터 세트를 학습 데이터와 테스트 데이터로 분리

# **데이터 세트 로딩**

# In[17]:


import pandas as pd


# In[6]:


# 붓꽃 데이터 세트 로딩
iris = load_iris()
print(iris)


# In[10]:


# iris.data : Iris 데이터 세트에서 
# 피처(feature)만으로 된 데이터를 numpy로 가지고 있음
iris_data = iris.data
print(iris_data[:10])


# In[15]:


# iris.target은 붓꽃 데이터 세트에서 
# 레이블(결정 값) 데이터를 numpy로 가지고 있음 (숫자)
# 레이블 = 결정값 = 정답(품종을 숫자로 표현)

iris_label = iris.target
print(iris_label)
print(iris.target_names)
print(iris.feature_names)


# In[19]:


# 붓꽃 데이터 DataFrame으로 변환 
iris_df = pd.DataFrame(data=iris_data, columns = iris.feature_names)
iris_df['label']= iris.target
iris_df.head()


# In[ ]:


###############################  참고  ####################################


# In[20]:


iris_df2 = iris_df
iris_df2.head()


# In[21]:


def label_name(label):
    if label == 0:
        name ='setosa'
    elif label == 1:
        name = 'versicolor'
    else:
        name = 'virginica'
        
    return name


# In[24]:


iris_df2['label_name']=iris_df2.apply(lambda x: label_name(x['label']), axis=1)


# In[25]:


iris_df2


# In[12]:





# In[13]:





# In[ ]:


###############################  참고  ####################################


# ### 학습 데이터와 테스트 데이터 세트로 분리

# **train_test_split() 함수** 사용
# * train_test_split(iris_data, iris_label, test_size=0.3, random_state=11)
# 
# 
# * train_test_split(피처 데이터 세트, 레이블 데이터 세트, 테스트 데이터 세트 비율, 난수 발생값)
#     * 피처 데이터 세트 : 피처(feature)만으로 된 데이터(numpy) [5.1, 3.5, 1.4, 0.2],...
#     * 레이블 데이터 세트 : 레이블(결정 값) 데이터(numpy) [0 0 0 ... 1 1 1 .... 2 2 2]  
#     * test_size(테스트 데이터 세트 비율) : 전체 데이터 세트 중 테스트 데이터 세트 비율 (0.3)
#     * random_state(난수 발생값) : 수행할 때마다 동일한 데이터 세트로 분리하기 위해 시드값 고정 (실습용)

# train_test_split() 반환값
# * X_train : 학습용 피처 데이터 세트  (feature)
# * X_test : 테스트용 피처 데이터 세트  (feature)
# * y_train : 학습용 레이블 데이터 세트 (target)
# * y_test : 테스트용 레이블 데이터 세트 (target)
# 
# * feature : 대문자 X_
# * label(target) : 소문자 y_

# In[26]:


#학습 데이터와 테스트 데이터 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.3, random_state=11)


# In[27]:


# 학습용 피처 데이터 세트
X_train[:10]


# In[28]:


# 테스트용 피처 데이터 세트
X_test[:10]


# In[29]:


# 학습용 레이블 데이터 세트
y_train[:10]


# In[30]:


# 테스트용 레이블 데이터 세트
y_test[:10]


# ### 학습 데이터 세트로 학습(Train) 수행

# ML 알고리즘으로 의사결정 트리 알고리즘을 이용해서 학습과 예측 수행  
# DecisionTreeClassifier 클래스의 fit()/predict() 메소드 사용  
# fit() : 학습 수행 (학습용 데이터)
#     - fit(학습용 피처 데이터, 학습용 레이블(정답) 데이터)
# predict() : 예측 수행
#     - predict(테스트용 피처 데이터)

# In[33]:


# DecisionTreeClassifier 객체 생성 
dt_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행 
dt_clf.fit(X_train, y_train)

# 학습용 피처 데이터, 학습용 레이블(정답) 데이터


# ### 테스트 데이터 세트로 예측(Predict) 수행

# In[35]:


# 학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행. 
pred = dt_clf.predict(X_test)

# 테스트용 피처 데이터


# In[21]:


pred


# ### 예측 정확도(accuracy) 평가

# - 예측 결과를 기반으로  
# - 의사 결정 트리 기반의 DecisionTreeClassifier의 예측 성능 평가  
# - 머신러닝 모델의 여러 성능 평가 방법 중 정확도 측정  
# - 정확도 : 예측 결과 실제 레이블 값과 얼마나 정확하게 맞는지 평가하는 지표

# - 예측한 붓꽃 품종과 실제 테스트 데이터 세트의 붓꽃 품종이 얼마나 일치하는지 확인 - 정확도 측정을 위해 사이킷런에서 제공하는 accuracy_score() 함수 사용  
#     - accuracy_score(실제 테스트용 레이블 데이터 세트, 예측된 레이블 데이터 세트)

# In[36]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)


# In[ ]:




