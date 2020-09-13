# scatter

> `scatter`는 **산점도**를 그려주는 그래프 중 하나이다.  여기서 **산점도**는 직교 좌표게를 이용해 두 개 변수 간의 관계를 나타내는 방법이다. 또한 산점도는 두 개 **변수** 간의 관계를 통해 **선형** 이나 **비선형**의 형태와 같은 수학적 모델을 확인해봄으로써 그 방향성과 강도를 조사할 수 있다.

* 다음과 같이 `matplotlib.pyplot`을 불러온다.

```python
import numpy as np
import matplotlib.pyplot as plt
```

* `random.randint`를 사용해 `x`, `y` data를 만든다. 

```python
np.random.seed(2)
sampleNum = 100 

x = np.random.randint(0,sampleNum,(sampleNum,))
y = np.random.randint(0,sampleNum,(sampleNum,))

x_mean = x.mean()
y_mean = y.mean()
```

* `scatter`를  이용해 그래프를 그려본다.

```python
plt.scatter(x,y,color='red')
plt.scatter(x_mean,y_mean,color='blue')

plt.show()
```

![image-20200913190316210](markdown-images/image-20200913190316210.png)