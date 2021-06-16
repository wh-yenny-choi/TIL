# Matplotlib

## Matplotlib의 이해



두가지 방식의 API 제공

- **API**(Application Programming Interface 애플리케이션 프로그래밍 인터페이스, 응용 프로그램 프로그래밍 인터페이스)는 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.

1. Pyplot API 
   - Matlab과 같이 커맨드 방식. matplotlib.pyplot 모듈에 함수로 정의되어 있음
2. 객체지향 API
   - matplotlib이 구현된 객체지향라이브러리를 직접 활용하는 방식

Pyplot API는 결국 객체지향API로 편의함수를 구현한 것으로, 세밀한 제어를 위해서는 객체지향 API를 사용해야함



matplotlib 객체지향 API 구성 객체

- FigureCanvas : 그림을 그릴 영역 나타내는 객체
- Renderer : 캔버스(FigureCanvas)에 그리는 도구 객체
- Artist : Renderer가 캔버스에 어떻게 그릴 것인가를 나타내는 객체

Rendererm, FigureCanvas는 사용자인터페이스 툴킷과 연계되는 낮은 수준의 제어를 담당

- wxPython, PostScript 등

Artist는 높은 수준 담당

- figure, text, line, patch등 
  - patch는 rectange, spline, path등을 모두 이르는 용어

즉, matplotlib사용자 입장에서는 Artist 객체를 다루는데 집중하면 된다. Artist는 두가지 유형으로 구분할 수 있다

1. Primitives
   - Line2D, Rectangle, Text, AxesImage, Patch 등과 같이 캔버스에 그려지는 표준 그래픽 객체
2. Containers
   - Axis, Axes, Figure 등과 같이 이들 primitives가 위치하게 될 대상

커맨더 방식이 아닌 객체지향 방식으로 그림을 그리는 표준적인 방법

- `Figure`객체를 생성
- `Figure`객체를 이용해 하나 이상의 `Axes`객체를 만들고
- `Axes`객체의 헬퍼함수로 primitives를 만들어 내는 것