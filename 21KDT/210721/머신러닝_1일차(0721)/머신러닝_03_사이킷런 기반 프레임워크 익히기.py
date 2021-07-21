!/usr/bin/env python
coding: utf-8

# 사이킷런 기반 프레임워크 익히기

## Estimator 클래스
- 머신러닝 모델(알고리즘) 클래스


- 학습을 위해서 fit()을 학습된 모델의 예측을 위해 predict()메서드를 제공
    - Estimator를 인자로 받는 함수는 Estimator의 fit()과 predict()를 호출해서 평가하거나 하이퍼파라미터 튜닝 수행
    - 평가함수 cross_val_score()
    - 하이퍼파라미터 튜닝 지원 클래스 GridSearchCV :  GridSearchCV.fit()


**지도학습**

![image.png](attachment:image.png)



**비지도학습**

- 차원축소, 클러스터링, 피처 추출 등을 구현한 클래스의 대부분이 fit()과 transform()을 적용
    - 피처 추출에서 fit()은 지도학습의 fit()과 같은 학습이 아니라 입력 데이터 형태에 맞춰 데이터를 변환하기 위한 사전 구조를 맞추는 작업
    - fit()으로 변환을 위한 사전구조를 맞추면 이후 입력 데이터의 차원 변환, 클러스터링, 피처 추출 등의 실제 작업은 transform()으로 수행함
    - fit()과 transform()을 하나로 결합한 fit_transform()

## 사이킷런의 주요 모듈

![image.png](attachment:image.png)

![image.png](attachment:image.png)

### 사이킷런 내장 예제 데이터

- dataset 모듈에 있는 여러 API를 호출하여 데이터 세트를 생성


![image.png](attachment:image.png)

###  인터넷에서 다운로드 받는 데이터
- fetch 계열 명령을 이용하여 다운로드
# - scikit_learn_data 서브 디렉터리 아래에 저장한 후 불러들이는 데이터
#
#
# - fetch_covtype() : 회귀분석용 토지 조사 자료
# - fetch_20newsgroups() : 뉴스 그룹 텍스트 자료
# - fetch_olivetti_faces() : 얼굴 이미지 자료
# - fetch_lfw_people() : 얼굴 이미지 자료
# - fetch_lfw_pairs() : 얼굴 이미지 자료
# - fetch_rcv1() : 로이터 뉴스 말뭉치
# - fetch_mldata() : ML 웹사이트에 다운로드

# ### 시뮬레이션 데이터 생성기
# - 분류(classification)와 군집분석(clustering)위한 표본 자료 생성
#
#
# - datasets.make_classifications()
#     - 분류를 위한 데이터 세트 생성
#     - 높은 상관도, 불필요한 속성 등의 노이즈 효과를 위한 데이터를 무작위로 생성
#
#
# - datasets.make_blobs()
#     - 클러스터링을 위한 데이터 세트를 무작위로 생성
#     - 군집 지정 개수에 따라 여러 가지 클러스터링을 위한 데이터 세트를 쉽게 만들어 줌

# ### 사이킷런의 내장 데이터 세트 구성과 의미

# In[1]:


from sklearn.datasets import load_iris


# In[3]:


iris_data = load_iris()
print(type(iris_data))


# In[6]:


keys = iris_data.keys()
print(keys)


# **사이킷런의 내장 데이터 세트 형태**
# * key 구성 : data, target, target_names, feature_names, DESCR
#
#     - data : 피처 데이터 세트 (ndarry)
#     - target : 분류(레이블 값)/회귀(숫자 결과값 데이터 세트) (ndarry)
#     - target_names : 개별 레이블 이름 (ndarry 또는 list)
#     - feature_names : 피처 이름 (ndarry 또는 list)
#     - DESCR : 데이터 세트 설명, 각 피처 설명 (string)
#
#     ![image.png](attachment:image.png)

# In[9]:


# data
print("data type", type(iris_data.data))
print("data shape", iris_data.data.shape)
print(iris_data['data'])


# In[10]:


# target
print("target type", type(iris_data.target))
print("target shape", iris_data.target.shape)
print(iris_data['target'])


# In[12]:


# target_names
print("target_names type", type(iris_data.target_names))
print("target_names shape", len(iris_data.target_names))
print(iris_data.target_names)


# In[13]:


# feature_names
print("featuret_names type", type(iris_data.feature_names))
print("feature_names shape", len(iris_data.feature_names))
print(iris_data.feature_names)


# In[11]:


# DESCR : 데이터 세트 설명, 각 피처 설명 (string)
iris_data.DESCR


# In[ ]:




