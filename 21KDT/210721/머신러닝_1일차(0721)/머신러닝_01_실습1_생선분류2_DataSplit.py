#!/usr/bin/env python
# coding: utf-8

# # 훈련 세트와 테스트 세트

# ### 생선 분류
# - 앞의 예에서 훈련데이터에서 도미를 100% 완벽하게 분류함
#     - 문제점 : 정답을 미리 알려주고 시험보는 것과 같음
#     
#     
# -  훈련한 데이터와 평가에 사용된 데이터가 달라야 함

# ## Data Split과 모델 검증
# 
# - 언제
#     - "충분히 큰" 데이터 세트를 가용할 때
#     - "충분히 큰" 데이터가 없을 때에는 교차 확인(Cross Validation) 고려
#     
# 
# - 왜
#     - 학습에 사용되지 않은 데이터를 사용하여 예측을 수행함으로써 모델의 일반적인 성능에 대한 적절한 예측을 함
#     
# 
# - 어떻게
#     - 홀드-아웃(Hold-out)
#     - 교차검증(Cross Validation,CV)
#     - 필요에 따라 Stratified Sampling

# ### 홀드-아웃 방식
# - 데이터를 두 개 세트로 나누어 각각 Train과 Test 세트로 사용
# - Train과 Test의 비율을 7:3 ~ 9:1로 널리 사용하나, 알고리즘의 특성 및 상황에 따라 적절한 비율을 사용
# - Train – Validation - Test로 나누기도 함
# 
# ![image.png](attachment:image.png)
# https://algotrading101.com/learn/train-test-split-2/

# ## 훈련 세트와 테스트 세트

# In[1]:


fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7,
               31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5,
               34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0,
               38.5, 38.5, 39.5, 41.0, 41.0, 
               9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2,
               12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0,
               475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0,
               575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0,
               920.0, 955.0, 925.0, 975.0, 950.0, 
               6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# In[2]:


fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14


# In[8]:


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()


# **훈련 데이터셋과 테스트 데이터셋으로 분리**

# In[9]:


train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]


# **학습 및 평가**

# In[10]:


kn.fit(train_input, train_target)
kn.score(test_input, test_target)


# In[14]:


print(train_target)


# In[15]:


print(test_target)


# ### 왜? 성능이 0.0일까?

# **편향(biased)된 데이터 셋 구성** 때문에
# 
# - 샘플링 편향(Sampling Bias)
# 
# ![image.png](attachment:image.png)

# ### 올바른 훈련데이터와 테스트데이터 구성하기

# In[16]:


import numpy as np


# In[17]:


input_arr = np.array(fish_data)
target_arr = np.array(fish_target)


# In[18]:


print(input_arr)


# In[19]:


print(input_arr.shape)


# ### 데이터 섞기(shuffling)
# 
# ![image.png](attachment:image.png)

# In[32]:


np.random.seed(42)
index = np.arange(49)
print(index)
np.random.shuffle(index)


# - [참고]: random.seed()
#     - 난수를 생성하기 위한 초기값 지정
#     - seed를 지정하면 랜덤함수의 결과를 동일하게 재현할 수 있음

# In[33]:


print(index)


# In[23]:


input_arr[[1, 3]]


# In[24]:


train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]


# In[26]:


print(input_arr[13], train_input[0])


# In[27]:


test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


# In[28]:


import matplotlib.pyplot as plt

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# ## 두 번째 머신러닝 프로그램

# In[34]:


kn.fit(train_input, train_target)


# In[35]:


kn.score(test_input, test_target)


# In[37]:


print(test_input)


# In[36]:


kn.predict(test_input)


# In[39]:


test_target

