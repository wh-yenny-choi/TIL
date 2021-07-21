#!/usr/bin/env python
# coding: utf-8

# # 데이터 전처리

# ## 넘파이로 데이터 준비하기

# In[2]:


fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# In[3]:


import numpy as np


# **두 리스트 열방향으로 합치기: 2차원 배열로**

# In[8]:


fish_data = np.column_stack((fish_length, fish_weight))


# In[9]:


print(fish_data[:5])


# **라벨 데이터**

# In[10]:


fish_target = np.concatenate((np.ones(35), np.zeros(14)))


# In[11]:


print(fish_target)


# ## 사이킷런으로 훈련 데이터와 테스트 데이터 나누기

# In[12]:


from sklearn.model_selection import train_test_split


# **train_test_split(매개변수들)**
# - *array : feature dataset, label dataset 
# - test_size = None 
# - train_size = None
# - shuffle = True
# - stratify = None
# - random_state = None

# In[13]:


train_input, test_input, train_target, test_target = train_test_split(fish_data,
                                                                      fish_target,
                                                                      random_state=42)


# In[15]:


test_input.shape


# In[17]:


train_target.shape


# In[20]:


test_target


# **데이터 분포를 반영한 분할**

# In[22]:


train_input, test_input, train_target, test_target = train_test_split(fish_data,
                                                                      fish_target,
                                                                      stratify = fish_target,
                                                                      random_state=42)


# In[23]:


test_target


# ## 성능 평가 및 테스트

# In[24]:


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)


# ### 도미 데이터 : 길이 25, 무게 150에 대한 분류 결과는?

# In[25]:


print(kn.predict([[25, 150]]))


# **테스트할 도미 데이터를 포함한 산점도**

# In[26]:


import matplotlib.pyplot as plt


# In[27]:


plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# **테스트할 도미데이터와 이웃하는 데이터들**

# In[29]:


dist, idx = kn.kneighbors([[25,150]])


# In[30]:


print(dist)


# In[31]:


print(idx)


# In[32]:


train_input[idx]


# In[33]:


plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[idx, 0], train_input[idx,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[35]:


print(train_target[idx])


# In[37]:


print(dist)


# ## 기준을 맞춰라

# In[38]:


plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[idx, 0], train_input[idx,1], marker='D')
plt.xlim((0,1000))
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# - 최근접이웃 알고리즘은 거리를 기반으로 가까운 이웃을 결정
# - 거리 계산 시 자료의 값이 큰 변수에 더 큰 영향을 받게 됨

# ### 두 변수의 스케일을 갖게
# - 표준점수(Z-Score)

# In[40]:


mean = np.mean(train_input, axis=0)
print(mean)


# In[41]:


std = np.std(train_input, axis=0)
print(std)


# In[45]:


train_scaled = (train_input-mean) / std
print(train_scaled[:10])


# In[47]:


plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# ### 전처리 데이터로 모델 훈련하기

# In[48]:


plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# **테스트 데이터도 스케일링**

# In[65]:


new = ([25, 150] - mean) / std
print(new)


# In[66]:


plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[60]:


kn.fit(train_scaled, train_target)


# In[61]:


test_scaled = (test_input - mean) / std


# In[62]:


kn.score(test_scaled, test_target)


# In[63]:


kn.predict([new])


# In[70]:


dist,idx = kn.kneighbors([new])
print(dist, idx)


# In[68]:


plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[idx,0], train_scaled[idx,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# In[ ]:




