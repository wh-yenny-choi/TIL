# Facebook Prophet

https://facebook.github.io/prophet/docs/installation.html

페이스북이 만든 시계열 예측 라이브러리 Prophet(예언자)

통계적 지식이 없어도 직관적 파라미터를 통해 모형을 조정할 수 있다.

일반적인 경우 기본값만 사용해도 높은 성능을 보여준다.



## The Prophet Forecasting Model

prophet 모형은 트렌트(growth), 계절성(seasonality), 휴일(holidays) 3가지의 main components로 이루어진다.
$$
y(t) = g(t) + s(t) + h(t) + epsilon_t
$$
영향력들 

- 트렌트(growth) : 비주기적 변화를 반영하는 추세함수

- 계절성(seasonality) : 주기적인 변화 (ex.주간, 연간)

- 휴일(holidays) : 휴일 (불규칙 이벤트)

- 오차항(epsilon<sub>t</sub>) : 모형이 설명하지 못하는 나머지 부분



prophet은 다른 시계열 모형과 달리 시간에 종속적인 구조를 가지지 않고 curve-fitting으로 예측 문제를 해결한다.

- ARIMA와 같은 시계열 모형은 시간에 종속적인 구조를 가진다.

 따라서 다음과 같은 이점을 얻는다.

1. 유연성 : 계절적 요소와 트렌드에 대한 가정을 쉽게 반영할 수 있다.
2. ARIMA 모델과 달리 모델을 측정 간격을 regularly spaced 할 필요가 없고, 결측이 있어도 상관없다.
3. 빠른 fitting 속도 -> 여러가지 시도를 할 수 있다
4. 직관적인 파라미터 조정을 위한 모델 확장이 쉽다.



### g(t), Growth, 트렌드

트렌드를 반영하기 위한 growth model로 두 가지를 소개한다.

- 첫 번째는 상한, 하한과 같은 한계점이 존재하는 경우(saturating growth model) 

- 두 번째는 없는 경우를 위한 모델로 각각 piecewise logistic model, piecewise linear model을 기반으로 한다.

#### Nonlinear, Saturating Growth

- 자연적 상한선이 존재하는 경우, Capacity가 있음
- Capacity는 시간에 따라 변화할 수 있음

아래의 그래프처럼 예측하고자 하는 값의 한계가 존재하는 경우 우리는 이를 반영한 모델을 세워야 한다.

![img](https://blog.kakaocdn.net/dn/TS9Ox/btqE2l6j4ad/TUVo5IBhhMyGelLLLm5Dy1/img.png)



#### Linear Trend with Changpoints (+change point)

![img](https://blog.kakaocdn.net/dn/nSAXi/btqE3d01DS1/WBgexATfSkC8YLkTmy7pDk/img.png)

앞의 경우와 달리 어떠한 한계가 존재하지 않는 예측 문제에 있어서 piecewise linear 모델은 간결하고 유용하다.

- Change Point는 자동으로 탐지
- 예측할 때는 특정 지점이 change point인지 여부를 확률적으로 결정



### s(t), Seasonality, 계절성

시계열 데이터는 인간의 행동에 의해서도 어떠한 주기성을 가질 수 있다.

- 예를 들어, 5-day work wek은 매주 반복되는 주간 시계열에 영향을 줄 수 있고, 방학은 연간 반복되는 효과를 주게 된다.

이러한 주기성을 시계열 모델에 반영하기 위해서는 시간에 주기적인 함수인 계절성(Seasonality) 모델이 필요하다.

사용자들의 행동 양식으로 주기적으로 나타나는 패턴

- 방학, 휴가, 온도, 주말 등등

푸리에 급수(Fourier Series)를 이용해 패턴의 근사치를 찾는다.



### h(t), Holidays and Events, 휴일

휴일과 이벤트들은 시계열 예측에 큰 영향을 미치지만 주기적 패턴을 따르지 않아 모델링하기가 어렵다.

하지만, 음력 행사라던지 추수감사절(11월 4번째 목요일)과 같은 비주기적인 휴일들이 시계열에 미치는 영향은 매년 비슷하기 때문에 모델에 반영되어야 한다.

여기서 이벤트의 효과는 독립이라고 가정하고 이벤트 앞뒤로 window 범위를 지정해 해당 이벤트의 영향력의 범위를 설정할 수 있다.

(크리스마스이브도 같이 크리스마스 효과에 반영하고 싶으면 lower_window를 -1로 설정)

주기성을 가지진 않지만 전체 추이에 큰 영향을 주는 이벤트가 존재한다.



## Model Fitting

- Stan을 통해 모델을 학습
  - probabilistic programming language for statistical inference
- 2가지 방식
  - MAP (Maximuam A Posteriori) : Default, 속도가 빠름
  - MCMC (Markov Chain Monte Carlo) : 모형의 변동성을 더 자세히 살펴볼 수 있음
- Analyst in the loop Modeling
  - 통계적 지식이 없어도 직관적 파라미터를 통해 모형을 조정할 수 있음
  - 일반적인 경우 기본값만 사용해도 높은 성능을 가능
  - 내부가 어떻게 동작하는지 고민할 필요가 없음
  - 요소
    - Capacities : 시계열 데이터 전체의 최대값
    - Change Points : 추세가 변화하는 시점
    - Holidays & Seasonality : 추세에 영향을 미치는 시기적 요인
    - Smoothing : 각각의 요소들이 전체 추이에 미치는 영향의 정도



## 정리

이렇게 분해가 가능한 모델의 중요한 이점은 예측의 각 구성요소를 확인할 수 있다는 점

아래처럼 트렌드와 계절성(주 단위, 연단위) component가 어떤 영향을 미치고 있는지 확인할 수 있는 그래프도 확인할 수 있으며, 이것으로 분석가들이 예측뿐만 아니라 예측 문제에 대해 다른 통찰력도 얻을 수 있을 거라고 한다.



### Holiday.ipynb

```sql
m = Prophet(holidays=holidays)  # 홀리데이 옵션을 넣어줌
forecast = m.fit(df_day).predict(future)
```

![다운로드 (3)](Facebook Prophet.assets/다운로드 (3).png)



### 한국의 holidys 옵션 추가

```sql
m = Prophet(holidays=holidays)  # 홀리데이 옵션을 넣어줌
m.add_country_holidays(country_name='KR')
forecast = m.fit(df_day).predict(future)
```

![한국 holidays (4)](Facebook Prophet.assets/한국 holidays (4).png)



https://m-insideout.tistory.com/m/13

https://zzsza.github.io/data/2019/02/06/prophet/
