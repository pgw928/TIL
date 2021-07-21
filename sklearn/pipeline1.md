## pipeline(1)

> `sklearn`에서 제공하는 표준적인 방법인 `Pipeline`과 간소화된 방법인 `make_pipeline` 함수에 대해서 알아본다.



### make_pipeline

> 별명을 사용하지 않고 pipeline을 만드는 간소화된 방법이다.



- 필요한 library

  ```python
  import numpy as np
  import pandas as pd
  from sklearn.preprocessing import StandardScaler
  from sklearn.datasets import load_boston
  from sklearn.pipeline import make_pipeline
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import SGDRegressor
  ```

  * `make_pipeline`은 `sklearn`의 `pipeline`에 포함되어 있다.

- data : boston data를 사용한다.

  ```python
  boston = load_boston()
  
  boston.keys()
  # dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
  
  type(boston['data'])
  # numpy.ndarray
  ```

  ```python
  boston_df = pd.DataFrame(boston['data'])
  boston_df['MEDV'] = boston['target']
  boston_df.head()
  ```

  ![image-20210722020654112](markdown-images/image-20210722020654112.png)

  ```python
  x_data, y_data = boston_df.iloc[:,:-1].values, boston_df['MEDV'].values
  x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=1)
  ```

- <u>`make_pipeline`으로 model pipeline 생성</u>

  ```python
  model = make_pipeline(StandardScaler(), SGDRegressor())
  model.steps
  # [('standardscaler', StandardScaler()), ('sgdregressor', SGDRegressor())]
  ```

  * pipeline을 생성할 함수들을 순차적으로 넣어준다.
  * 명칭이 함수명의 소문자로 명명된다.

* 학습 및 결과

  ```python
  model.fit(x_train, y_train)
  # Pipeline(steps=[('standardscaler', StandardScaler()),
  #                 ('sgdregressor', SGDRegressor())])
  ```

  ```python
  print(model.score(x_train, y_train)) # 0.7285343223205636
  print(model.score(x_test, y_test)) # 0.7627524208353504
  ```

  * 학습 결과에 초점을 맞추지는 말자..

