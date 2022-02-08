# Attention Is All You Need

https://arxiv.org/abs/1706.03762

RNN, CNN이 아닌 새로운 구조

- RNN : 반복적이고 순차적인 학습에 특와된 인공신경망의 한 종류, 내부 순환구조의 특징이 있다.
- CNN : 데이터의 특징을 추출하여 특징들의 패턴을 파악하는 구조

FNN과 skip connection 기반의 모듈을 N개 쌓아서 LSTM, GRU 같은 아키텍처 없이도 long-term dependency를 해결한 새로운 인코더, 디코더 방식이라는 점

기존 affine transformation 방식의 attention이 두 벡터 사이의 "연관성"에 관련해서 어떤 방식으로 작동하는지 헷갈리는 것을 dot product방식으로 개선하였다.



attention만으로도 encoder-decoder 구조를 가진 모델

![img](https://media.vlpt.us/images/skm0626/post/81ac75d6-e51f-411e-9afe-0c0db87225e2/image.png)



## 







https://hipgyung.tistory.com/entry/ATTENTION-IS-ALL-YOU-NEED-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0

https://velog.io/@skm0626/Attention-Is-All-You-NeedTransformer-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0

https://dalpo0814.tistory.com/49

https://pozalabs.github.io/transformer/

